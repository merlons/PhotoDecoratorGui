import pathlib

from PySide6.QtCore import QThread
from PySide6.scripts.metaobjectdump import Signal

import init
from entity.config import Config, ElementConfig
from entity.image_container import ImageContainer
from entity.image_processor import ProcessorChain
from enums.constant import LOCATION_LEFT_TOP, LOCATION_LEFT_BOTTOM, LOCATION_RIGHT_TOP, LOCATION_RIGHT_BOTTOM, DEBUG
from ui.tools.logger import logger
from utils import get_file_list, ENCODING


class Config(Config):

    def set_input_dir(self, path):
        self._data['base']['input_dir'] = path

    def set_output_dir(self, path):
        self._data['base']['output_dir'] = path

    def set_left_top(self, value):
        self._data['layout']['elements']['left_top']['name'] = value

    def set_left_bottom(self, value):
        self._data['layout']['elements']['left_bottom']['name'] = value

    def set_right_top(self, value):
        self._data['layout']['elements']['right_top']['name'] = value

    def set_right_bottom(self, value):
        self._data['layout']['elements']['right_bottom']['name'] = value

    def get_left_top(self) -> ElementConfig:
        return ElementConfig(self._data['layout']['elements'][LOCATION_LEFT_TOP])

    def get_left_bottom(self) -> ElementConfig:
        return ElementConfig(self._data['layout']['elements'][LOCATION_LEFT_BOTTOM])

    def get_right_top(self) -> ElementConfig:
        return ElementConfig(self._data['layout']['elements'][LOCATION_RIGHT_TOP])

    def get_right_bottom(self) -> ElementConfig:
        return ElementConfig(self._data['layout']['elements'][LOCATION_RIGHT_BOTTOM])





class WorkerThread(QThread):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    def update_config(self, config):
        config.set_input_dir(self.kwargs.get('input_dir'))
        config.set_output_dir(self.kwargs.get('output_dir'))

        layout = [
            'watermark_left_logo',
            'watermark_right_logo',
            'dark_watermark_left_logo',
            'dark_watermark_right_logo',
        ]
        left_top = ['Model', 'Make', 'LensModel', 'Param', 'Datetime']
        left_bottom = left_top
        right_top = left_top
        right_bottom = left_top

        config.set_layout(layout[self.kwargs.get('layout')])
        config.set_left_top(left_top[self.kwargs.get('left_top')])
        config.set_left_bottom(left_bottom[self.kwargs.get('left_bottom')])
        config.set_right_top(right_top[self.kwargs.get('right_top')])
        config.set_right_bottom(right_bottom[self.kwargs.get('right_bottom')])

        config.enable_shadow() if self.kwargs.get('shadow') else config.disable_shadow()
        config.enable_white_margin() if self.kwargs.get('white_margin') else config.disable_white_margin()
        config.enable_logo() if self.kwargs.get('logo_enable') else config.disable_logo()
        config.enable_padding_with_original_ratio() if self.kwargs.get(
            'padding_with_original_ratio') else config.disable_padding_with_original_ratio()
        config.enable_equivalent_focal_length() if self.kwargs.get(
            'use_equivalent_focal_length') else config.disable_equivalent_focal_length()
        # config.save()

        init.EMPTY_PROCESSOR.config = config
        init.WATERMARK_PROCESSOR.config = config
        init.WATERMARK_LEFT_LOGO_PROCESSOR.config = config
        init.WATERMARK_RIGHT_LOGO_PROCESSOR.config = config
        init.MARGIN_PROCESSOR.config = config
        init.SHADOW_PROCESSOR.config = config
        init.SQUARE_PROCESSOR.config = config
        init.SIMPLE_PROCESSOR.config = config
        init.PADDING_TO_ORIGINAL_RATIO_PROCESSOR.config = config
        init.BACKGROUND_BLUR_PROCESSOR.config = config
        init.BACKGROUND_BLUR_WITH_WHITE_BORDER_PROCESSOR.config = config
        init.PURE_WHITE_MARGIN_PROCESSOR.config = config

    def run(self):
        config = Config('config.yaml')
        self.update_config(config)

        file_list = get_file_list(config.get_input_dir())
        print('当前共有 {} 张图片待处理'.format(len(file_list)))

        processor_chain = ProcessorChain()

        # 如果需要添加阴影，则添加阴影处理器，阴影处理器优先级最高，但是正方形布局不需要阴影
        if config.has_shadow_enabled() and 'square' != config.get_layout_type():
            processor_chain.add(init.SHADOW_PROCESSOR)

        # 根据布局添加不同的水印处理器
        if config.get_layout_type() in init.layout_items_dict:
            processor = init.layout_items_dict.get(config.get_layout_type()).processor
            processor.config = config
            processor_chain.add(processor)
        else:
            processor_chain.add(init.SIMPLE_PROCESSOR)

        # 如果需要添加白边，且是水印布局，则添加白边处理器，白边处理器优先级最低
        if config.has_white_margin_enabled() and 'watermark' in config.get_layout_type():
            processor_chain.add(init.MARGIN_PROCESSOR)

        # 如果需要按原有比例填充，且不是正方形布局，则添加填充处理器
        if config.has_padding_with_original_ratio_enabled() and 'square' != config.get_layout_type():
            processor_chain.add(init.PADDING_TO_ORIGINAL_RATIO_PROCESSOR)

        for source_path in file_list:
            # 打开图片
            container = ImageContainer(source_path)

            # 使用等效焦距
            container.is_use_equivalent_focal_length(config.use_equivalent_focal_length())

            # 处理图片
            try:
                processor_chain.process(container)
            except Exception as e:
                logger.error(f'Error: {str(e)}')
                if DEBUG:
                    raise e

            # 保存图片
            target_path = pathlib.Path(config.get_output_dir(), encoding=ENCODING).joinpath(source_path.name)
            container.save(target_path, quality=config.get_quality())
            container.close()
            logger.info(f"{source_path} >> {target_path}")
        logger.info(f"处理完成，文件已输出至{config.get_output_dir()}文件夹中")

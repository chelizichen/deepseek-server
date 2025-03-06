from conf.conf import SgridConfig

def init_config():
    new_config = SgridConfig()
    new_config.init_config()
    return new_config


sgrid_config = init_config()
from src.modules.modx.container import ModXContainer
from src.modules.mody.container import ModYContainer

def init_resources():
    #instances
    modx_container = ModXContainer()
    mody_container = ModYContainer()    
    
    #init containers
    modx_container.init_resources()
    mody_container.init_resources()
    
    
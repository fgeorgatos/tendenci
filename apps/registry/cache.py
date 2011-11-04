from django.core.cache import cache
from registry.utils import RegisteredApps
import pickle

REGISTRY_PRE_KEY = "registry"

def delete_reg_apps_cache():
    """
        Delete cache for all apps
    """
    keys = [REGISTRY_PRE_KEY, 'reg_apps']
    key = '.'.join(keys)
    cache.delete(key)

def cache_reg_apps(apps):
    """
        Caches the list of registered apps
    """
    keys = [REGISTRY_PRE_KEY, 'reg_apps']
    key = '.'.join(keys)
    
    #pickle the RegisteredApps Object
    value = apps.all_apps
    
    cache.set(key, value)

def get_reg_apps():
    """
        Gets all the registered apps from the cache
    """
    keys = [REGISTRY_PRE_KEY, 'reg_apps']
    key = '.'.join(keys)
    
    all_apps = cache.get(key)
    
    return all_apps
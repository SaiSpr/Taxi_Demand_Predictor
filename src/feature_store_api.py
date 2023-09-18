from typing import Optional
import hsfs
import hopsworks

import src.config as config

def get_feature_store() -> hsfs.feature_store.FeatureStore:
    """Connects to Hopsworks and returns a pointer to the feature store

    Returns:
        hsfs.feature_store.FeatureStore: pointer to the feature store
    """
    project = hopsworks.login(
        project = 'sai_project_1',
        api_key_value = jw7nD5pVpCMjt7xz.JoUh1fdEUFNCJyUa5n7VsdR67C9PZCyVonuZ4eNafUCJzMJbDt6V0LxfyghCD794
    )
    return project.get_feature_store()

def get_feature_group(
    name: str,
    version: Optional[int] = 1
    ) -> hsfs.feature_group.FeatureGroup:
    """Connects to the feature store and returns a pointer to the given
    feature group `name`

    Args:
        name (str): name of the feature group
        version (Optional[int], optional): _description_. Defaults to 1.

    Returns:
        hsfs.feature_group.FeatureGroup: pointer to the feature group
    """
    return get_feature_store().get_feature_group(
        name=name,
        version=version,
    )

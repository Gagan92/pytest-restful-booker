import yaml


def read_yml(filepath):
    """
    This method returns the contents of the yaml file
    :param filepath: yaml filepath
    :type filepath: str
    :return: contents
    """
    with open(filepath, 'r') as file:
        yml_contents = yaml.safe_load(file)
        return yml_contents

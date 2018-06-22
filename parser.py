import yaml
yaml_dict = yaml.load(open('tile-metadata.yml'))

print yaml_dict['stemcell_criteria']['version']

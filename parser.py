import yaml
yaml_dict = yaml.load(open('blah.yml'))

print yaml_dict['stemcell_criteria']['version']

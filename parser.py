import yaml
import sys

yaml_dict = yaml.load(open(sys.argv[1]))

print yaml_dict['stemcell_criteria']['version']

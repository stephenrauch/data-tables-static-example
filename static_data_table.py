import jinja2
import json
import os

# base filenames and directories on this file
file_dir = os.path.dirname(__file__)
data_file = os.path.join(file_dir, 'data.json')
base_file_name = os.path.basename(__file__[:-3])
template_file = f'{base_file_name}.template.html'
output_file = f'{file_dir}/build/{base_file_name}.html'

# load the data into a context
with open(data_file) as f:
    context = json.load(f)
context.update(dict(
    table_id = 'data_table',
    page_title='Static Data Table Html Gen'
))

# init jinja2 template
loader = jinja2.FileSystemLoader(file_dir)
env = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template(template_file)

# feed the context to the template and generate an HTML file
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    f.write(template.render(**context))

from flask import render_template
from flask import request
from jira_graph_viz import jira_graph_viz
from jira_graph_viz.forms import QueryForm
from jira_graph_viz.query_controller import submit_query
from jira_graph_viz_config import Configs

@jira_graph_viz.route('/', methods=['GET','POST'])
@jira_graph_viz.route('/index', methods=['GET','POST'])
def index():
	form = QueryForm()
	query = request.args.get('query')

	dataset = {}
	links = {}
	query_list = []
	jira_base_url = ''

	if form.validate_on_submit():
		dataset,links,query_list,jira_base_url = submit_query(form.query.data)
	elif query:
		dataset,links,query_list,jira_base_url = submit_query(query)
	print("jira_base_url {}".format(jira_base_url))
	return render_template('index.html',
						   form = QueryForm(),
						   dataset = dataset,
						   links = links,
						   query_list = query_list,
						   jira_base_url = jira_base_url)


@jira_graph_viz.route('/health', methods=['GET'])
def health():
	return 'JIRA-GRAPH-VIZ Online'

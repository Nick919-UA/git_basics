import argparse
from helpers.github import get_github_repositories, json_parser
from helpers.writter import write

parser = argparse.ArgumentParser()

parser.add_argument("-q", dest="query")
parser.add_argument("-p", dest="page")

args = parser.parse_args()

body = get_github_repositories(args.query, args.page)
repositories = json_parser(body)
write(repositories)
print("Done!")

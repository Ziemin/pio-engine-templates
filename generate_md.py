import yaml
import sys
import urllib.parse as urlparse

INTRO = \
"""\
![alt text](https://github.com/apache/incubator-predictionio/blob/develop/docs/manual/source/images/logos/logo.png)

# Engine Templates

* [Classification](#classification)
* [Regression](#regression)
* [Unsupervised Learning](#unsupervised-learning)
* [Recommender Systems](#recommenders)
* [Natural Language Processing](#nlp)
"""
UNSUPERVISED = \
"""
<div id='unsupervised-learning'/>

## Unsupervised Learning
"""
CLASSIFICATION = \
"""
<div id='classification'/>

## Classification
"""

REGRESSION = \
"""
<div id='regression'/>

## Regression
"""

RECOMMENDER_SYSTEMS = \
"""
<div id='recommenders'/>

## Recommender Systems
"""

NLP = \
"""
<div id='nlp'/>

## Natural Language Processing
"""

TEMPLATE_INTRO = \
"""#### ***[{name}]({repo})***"""

STAR_BUTTON = \
"""\
<iframe src="https://ghbtns.com/github-btn.html?user={user}&repo={repo}&\
type=star&count=true" frameborder="0" align="right" scrolling="0" width="170px" height="20px"></iframe>

"""

TEMPLATE_DETAILS = \
"""
{description}

Type | Language | License | Status | PIO min version
:----: | :-----:| :-----: | :----: | :-------------:
{type} | {language} | {license} | {status} | {pio_min_version}

"""

class Template:

    def __init__(self, engine):
        for key, val in engine.items():
            setattr(self, key, val)

        self.tags = list(map(lambda s: s.lower(), self.tags))
        self.has_github = True if self.parse_github() else False

    def parse_github(self):
        pr = urlparse.urlparse(self.repo)
        if pr.netloc == 'github.com':
            path = pr.path.split('/')
            assert(len(path) >= 3)
            self.github_user = path[1]
            self.github_repo = path[2]
            return True
        else:
            return False

def write_template(readme, template):
    intro = TEMPLATE_INTRO.format(
                name=template.name,
                repo=template.repo)
    if template.has_github:
        intro += STAR_BUTTON.format(
                    user=template.github_user,
                    repo=template.github_repo)
    readme.write(intro)
    readme.write(TEMPLATE_DETAILS.format(
            description=template.description,
            type=template.type,
            language=template.language,
            license=template.license,
            status=template.status,
            pio_min_version=template.pio_min_version,
        ))

def write_templates(readme, templates):
    for t in templates:
        write_template(readme, t)

def write_markdown(readme, templates):
    classification = [engine for engine in templates if "classification" in engine.tags]
    regression = [engine for engine in templates if "regression" in engine.tags]
    unsupervised = [engine for engine in templates if "unsupervised" in engine.tags]
    recommenders = [engine for engine in templates if "recommender" in engine.tags]
    nlps = [engine for engine in templates if "nlp" in engine.tags]

    readme.write(INTRO)

    readme.write(CLASSIFICATION)
    write_templates(readme, classification)

    readme.write(REGRESSION)
    write_templates(readme, regression)

    readme.write(UNSUPERVISED)
    write_templates(readme, unsupervised)

    readme.write(RECOMMENDER_SYSTEMS)
    write_templates(readme, recommenders)

    readme.write(NLP)
    write_templates(readme, nlps)


if __name__ == "__main__":

    with open(sys.argv[1], 'r') as stream:
        templates = yaml.load(stream)
        parsed = [Template(position["template"]) for position in templates]

        with open("README.md", 'w') as readme:
            write_markdown(readme, parsed)

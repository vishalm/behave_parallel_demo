<p>
  <a href="https://twitter.com/intent/follow?screen_name=vishalm84"><img align="left" src="https://img.shields.io/twitter/follow/vishalm84.svg?style=social&label=Follow%20@vishalm84" alt="Follow on Twitter"></a>
<br />
</p>

[![Build Status](https://dev.azure.com/vishalmishra84/Test%20Project/_apis/build/status/vishalm.behave_parallel_demo?branchName=master)](https://dev.azure.com/vishalmishra84/Test%20Project/_build/latest?definitionId=2&branchName=master)

[![Travis](https://travis-ci.org/vishalm/behave_parallel_demo.svg)](https://travis-ci.org/vishalm/behave_parallel_demo)



# Welcome to the behave_parallel_demo wiki!
#### Must do 
How what want to manage virtual env but make sure you are following these steps
* `virtualenv .env `
* `source .env/bin/activate `
* `pip install -r requirements.txt`
* `pip install  git+git://github.com/hugeinc/behave-parallel.git@a57eff3087aae9bd7519a7d4fc15228611db20b9#egg=behave-parallel --upgrade` ### Super importent


##Works exact steps on Ubuntu:

### Steps: 
1. Clone this repo 
1. Goto to root of the project
1. Create a virtual evn 

* `virtualenv .env `
* `source .env/bin/activate `
* `pip install -r requirements.txt`
* `pip install  git+git://github.com/hugeinc/behave-parallel.git@a57eff3087aae9bd7519a7d4fc15228611db20b9#egg=behave-parallel --upgrade` ### Super importent
* `pip freeze`

###Run Features in parallel
`/usr/bin/time behave --processes 5 --parallel-element feature `

###Run Scenario in parallel
`/usr/bin/time behave --processes 5 --parallel-element scenario `

###How I run feature: 
`/usr/bin/time behave --processes "${PROCESS_COUNT}" --parallel-element feature --junit --junit-directory=xmlrunner -v -t "${TAGS_LIST}" -f rerun -o rerun.txt -f plain -T --no-skipped --tags=~@xfail features/`

###How I run Scenario: 
`/usr/bin/time behave --processes "${PROCESS_COUNT}" --parallel-element scenario --junit --junit-directory=xmlrunner -v -t "${TAGS_LIST}" -f rerun -o rerun.txt -f plain -T --no-skipped --tags=~@xfail features/ `

Actual Source:

<https://github.com/vishalm/behave-parallel/blob/upstreamsync/README.md>

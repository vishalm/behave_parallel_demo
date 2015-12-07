Works exact steps on Ubuntu:

Steps:
Clone this repo
Goto to root of the project
Create a virtual evn
    virtualenv .env
    source .env/bin/activate
    pip install -r requirements.txt


Run Features in parallel
/usr/bin/time behave --processes 5 --parallel-element feature

Run Scenario in parallel
/usr/bin/time behave --processes 5 --parallel-element scenario

How I run feature:
/usr/bin/time behave --processes "${PROCESS_COUNT}"  --parallel-element feature --junit --junit-directory=xmlrunner -v -t "${TAGS_LIST}" -f rerun -o rerun.txt -f plain -T --no-skipped --tags=~@xfail features/


How I run Scenario:
/usr/bin/time behave --processes "${PROCESS_COUNT}"  --parallel-element scenario --junit --junit-directory=xmlrunner -v -t "${TAGS_LIST}" -f rerun -o rerun.txt -f plain -T --no-skipped --tags=~@xfail features/



Advice
Ultimately this is probably the way you want to run it most of the time:

behave --processes 4 --parallel-element scenario --junit --show-timings --logging-level INFO


Actual Source:
https://github.com/vishalm/behave-parallel/blob/upstreamsync/README.md
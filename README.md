# MachineLearningAssignmentOne

### Clone Repository

Clone the repository
```
git clone https://github.com/shahrukhzarir/MachineLearningAssignmentOne.git
```

### Installing and Set Up

Install Required Packages:
```
pip install -r requirements.txt
```

Adjust Setup Files:

```
vim setup.py
```

Change Items Accordingly To Your Information:
```py
try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

config = {
	'description': 'package description',
	'author': 'Enter Name Here',
	'author_email': 'Enter Email Here',
	'version': '0.0.1',
	'packages': find_packages(),
	'name': 'package_name'
}
setup(**config)
```

Once setup.py is modified build and install item:

```
python setup.py build
python setup.py install
```
### Running The Code

You can now run the code by doing the following:

```
cd api
python scrape.py
```

You will now see a csv file called player.csv, you can view the data by:

```
cat player.csv
GROUP_SET,GROUP_VALUE,TEAM_ID,TEAM_ABBREVIATION,MAX_GAME_DATE,GP,W,L,W_PCT,MIN,FGM,FGA,FG_PCT,FG3M,FG3A,FG3_PCT,FTM,FTA,FT_PCT,OREB,DREB,REB,AST,TOV,STL,BLK,BLKA,PF,PFD,PTS,PLUS_MINUS,NBA_FANTASY_PTS,DD2,TD3,GP_RANK,W_RANK,L_RANK,W_PCT_RANK,MIN_RANK,FGM_RANK,FGA_RANK,FG_PCT_RANK,FG3M_RANK,FG3A_RANK,FG3_PCT_RANK,FTM_RANK,FTA_RANK,FT_PCT_RANK,OREB_RANK,DREB_RANK,REB_RANK,AST_RANK,TOV_RANK,STL_RANK,BLK_RANK,BLKA_RANK,PF_RANK,PFD_RANK,PTS_RANK,PLUS_MINUS_RANK,NBA_FANTASY_PTS_RANK,DD2_RANK,TD3_RANK,CFID,CFPARAMS
Overall,2017-18,1610612745,HOU,2018-01-30T00:00:00,42,32,10,0.762,36.1,9.4,21.0,0.449,4.1,10.5,0.386,8.7,10.1,0.861,0.6,4.5,5.0,9.1,4.4,1.9,0.7,1.4,2.5,7.0,31.6,6.9,54.5,19,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,265,2017-18
```


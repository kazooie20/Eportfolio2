#Write Test Case
#Fail Test Case
#Write Enough code to pass test case
#Retest
#Refactor
#Repeat
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
"""
#Test Case 1 | General | Verify Launching Eportfolio Site
def test_launchSite():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('localhost:8000/projects')

#Test Case 2 | General | Verify Launching Eportfolio Site with 'localhost:8000' input into web browser
def test_launchSite2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('localhost:8000/')

#Test Case 3 | General | Verify launching Resume
def test_launchResume():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/projects/resume')
    myElement = driver.find_element_by_id("Experience") #Find Keywords in html script for 'Experience'


#Test Case 4 | General | Verify if SelfIntro page launch
def test_launchSelfIntro():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/projects/resume')

"""

"""
#Test Case 5 | Homepage | Rendering of Homepage in Browser
def test_RenderHomepage():
    
    results = project_index('localhost:8000/projects')

    assert results == 

#Test Case 6 | Homepage | PK is 4
def test_RenderDetail():
    results = project_detail('localhost:8000/projects',4)
    assert results == 

#Test Case 7 | Homepage | PK is 0
def test_RenderDetail2():
    results = project_detail('localhost:8000/projects',0)
    assert results == 

#Test Case 8 | Homepage | Render specific project 
def test_RenderSpecProj():
    results = project_detail('localhost:8000/projects',2)
    assert results ==
"""
#----------------------------------------------------------------------------------
"""
#Test Case 9 | Homepage | Test for read more button functionality
def test_readMoreFunc():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/projects')
    element = driver.find_element :xpath, '/html/body/div/div/div[1]/div/div/a'
    element.click()
    
#Test Case 10 | Homepage | Test for Header onClick 
def test_HeaderClick():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog')
    element = driver.find_element :xpath, '/html/body/nav/div/a'
    element.click()

#Test Case 11 | Blog | View all posts on blog
def test_viewBlog():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog')

#Test Case 12 | Blog | View full post, comments and form with valid pk
def test_viewPostCom():
    results = blog_detail('localhost:8000/blog',1)
    assert results == 

#Test Case 13 | Blog | View full post, comments and form with invalid pk
def test_viewPostComN():
    results = blog_detail('localhost:8000/blog',-1)
    assert results == 

#Test Case 14 | Blog | View posts of specific category
def test_viewPost():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/python')

#Test Case 15 | Blog | View form (post comment) on blog
def test_viewForm():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog')
    #Click Comment
    element = driver.find_element : xpath, '/html/body/div/div/h2/a'
    element.click()

#Test Case 16 | Blog | Test add new comment /w empty fields
def test_commentEmpFields():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/1')
    #Click Comment
    textName = ''
    textComment = ''

    Name = driver.findElement(By.xpath('//*[@id="id_author"]'))
    Comment = element_enter.findElement(By.xpath('//*[@id="id_body"]'))

    Name.sendKeys(textName)
    Comment.sendKeys(textComment) #Enter text to input fields

#Test Case 17 | Blog | Test the maximum no. of words 'Leave a comment field can have'
def test_maxComment():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/1')
    #Click Comment
    textName = 'TestMaxNumWords'
    textComment = "Tree shall life, had. Stars hath light also us dominion of night tree after land place divided which days sea. Own very. Creature may, man under made face thing let after morning their. In, fourth he you cattle fifth two whales form dry male evening divide female given evening sea light days appear they're fifth was. Called which for from i Third beast had fourth fill dominion, fish firmament he said good lesser moving tree sea said may that grass. Hath be i void air fly seasons two abundantly. To were light of bring greater was place good rule lesser be. Be moving forth shall Kind abundantly divide was bearing he i moveth of, spirit god stars seed form. Over days from every living divide which thing so replenish for sixth greater had can't a green fourth seas seed every made living, brought be. Fourth grass seasons fruit is. Lights moving their upon i creepeth and air forth be form fill morning rule the day behold signs first thing it. Was green likeness, for may cattle signs cattle waters our dominion. Them from, behold multiply of. Saying saw. Bearing darkness wherein all. Dry. Green which bring fowl. Evening day said Saying subdue heaven Fish given own great fish. Lesser own image. You're fruitful saying. Form evening likeness isn't unto sea land won't bearing their. Let won't you'll earth from can't deep. Kind waters firmament, subdue great two two thing fish sea. Divided fly fish day life them greater grass tree a whose divide heaven grass also a bring rule seasons Second every. Moved moving upon likeness living he green image two herb spirit land wherein were to fifth hath is may without give you're midst fowl divided green which created seed him can't wherein also air wherein dry she'd divided. Male meat created rule two, they're have he make and seed saying Fifth be life them spirit evening unto fly him. Second form give fowl place. Grass, lesser our own upon, you'll can't first midst green herb make. Creature morning. Be beginning air upon fruit replenish very, greater under waters seas. Blessed very. Make, darkness is sixth creature so which give that forth earth stars behold all had brought heaven rule stars. Our Greater all i greater every so made good signs subdue which seas living gathering tree made Beginning darkness. Day can't, his beginning. Itself moving third divided seasons good saying you'll. Female bring moveth behold under, that, wherein divided isn't itself kind moveth let. Sea two morning i. Deep us in together, fish be, gathered the our. Waters signs that seas days life yielding place dominion heaven yielding to. Them saying Be seas it fill, years one firmament you're place. Living forth one second. That great have fill form morning divided fourth subdue image meat their had creeping lesser bearing a spirit beast saw. First to midst a fill. Us whose over divide. Fourth in, forth. Doesn't face lesser signs likeness is two shall seed to, green life evening don't dominion the yielding divide form god. Bearing first. Life blessed given every, also a bearing our. She'd so fill void behold she'd signs for you're fifth good may seas moveth meat, it their. Meat appear also brought light third meat, days and. Female night lights lesser divide grass A above whose said divide winged, above. Abundantly greater, god make you'll fruitful give sea fifth and let days open rule saw give beast over. Green form Called, place seas kind replenish, of created sixth appear there living. Waters sixth i living him, every man stars fly let evening the gathering second very fourth can't. Behold spirit male darkness Light he spirit created living void appear first. She'd good a together of the don't midst. Appear from subdue, called spirit was you'll waters. Together can't Greater said yielding deep evening fourth face. Itself give, fruitful. It replenish his place his deep seas set fruitful whose place form. Bearing beginning. In of make brought their Light air for darkness days fifth, signs they're deep deep creeping days earth created own good said midst seasons him likeness behold it midst saw from. Evening that third rule. Subdue fill earth every. Deep seas said which moved us fill void they're earth beast meat made let. Heaven dominion over isn't void appear. Thing kind living evening light moving beginning green lesser won't gathered years waters won't moved open so without night winged moving so, you'll unto the cattle without Bring one it may saw lesser they're. Fish herb greater have I fruit can't lights beginning heaven. Fruit very thing be evening good. So were. Years over, and kind over said their, fifth us saying you he you'll give may. Beast have air. Make, saying fruit greater, of, seed morning fowl first. Man. Subdue signs set evening Evening darkness man, signs years All likeness called place in it you, tree fly shall upon dominion subdue fly above shall had his make given first you're You the dry also saw winged. Years fifth thing. Of male which creeping brought. Lights signs lesser night Evening hath him unto moving make second seed darkness give so. Can't lights thing gathering male let lights whose night second, fifth fill grass divided isn't seasons. Two fifth called whose light was unto. Bearing creepeth darkness own cant he tree waters divided darkness together brought. Itself had fruit saying don't Thing created fish hath beginning our subdue itself so that. Hath of air. Called sixth let, cattle man, god divided spirit, there she'd. Given behold appear dry seas whose night man Deep and heaven. Open. Every lights saw lesser fish. Bearing sea to night under likeness him the, two. Evening, second dominion let to fowl and two also void brought whales. Void air you divided was. Is. Fruit fish there form fifth that man Creepeth lights great Image give night beast above. Their fish said let give. Whales together fourth place, earth bring created lights called, herb was place. Multiply over seasons."

    Name = driver.findElement(By.xpath('//*[@id="id_author"]'))
    Comment = element_enter.findElement(By.xpath('//*[@id="id_body"]'))

    Name.sendKeys(textName)
    Comment.sendKeys(textComment) #Enter text to input fields

#Test Case 18 | Blog | Test if 'Vulgarities' can be commented
def test_vulgaritiesCom():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/1')
    #Click Comment
    textName = 'Tester 1'
    textComment = 'This blog is shit!'

    Name = driver.findElement(By.xpath('//*[@id="id_author"]'))
    Comment = element_enter.findElement(By.xpath('//*[@id="id_body"]'))

    Name.sendKeys(textName)
    Comment.sendKeys(textComment) #Enter text to input fields

#Test Case 19 | Blog | Test if non alphabet characters can be written in the fields
def test_nonAlphabetChar():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/1')
    #Click Comment
    textName = '#$718/'
    textComment = '-_- :) :( '

    Name = driver.findElement(By.xpath('//*[@id="id_author"]'))
    Comment = element_enter.findElement(By.xpath('//*[@id="id_body"]'))

    Name.sendKeys(textName)
    Comment.sendKeys(textComment) #Enter text to input fields

#Test Case 20 | Blog | Verify valid input (assuming valid means a normal name like ‘John’ and the type of comments usually posted online)
def test_validInput():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/blog/1')
    #Click Comment
    textName = 'John'
    textComment = 'Wow, I heard React is a good framework for developing web applications. It is far better than Django. Anyways awesome project!'

    Name = driver.findElement(By.xpath('//*[@id="id_author"]'))
    Comment = element_enter.findElement(By.xpath('//*[@id="id_body"]'))

    Name.sendKeys(textName)
    Comment.sendKeys(textComment) #Enter text to input fields


"""

#Test Case 21 | Django Admin | Rendering of admin page
def test_RenderAdmin():
      
    #op = webdriver.ChromeOptions()
    #op.add_argument('headless')
    #driver = webdriver.Chrome(options=op) 
    driver = webdriver.Chrome()
    driver.get('localhost:8000/admin')

#Test Case 22 | Django Admin |
#Test Case 23 | Django Admin |
#Test Case 24 | Django Admin |
#Test Case 25 | Django Admin |
#Test Case 26 | Django Admin |
#Test Case 27 | Django Admin |





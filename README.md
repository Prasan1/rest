# rest
Project Descriptions:
---------------------

The mysql database will contains many fields and a JSONField. JSONField is the Json data of all other fileds in json form. e.g

id | squad_name | hometown | active | formed | members

All the columns above take their respective value but the members column will store json data that is build by all other columns. eg.

id | squad_name| hometown|active| formed | members
-------------------------------------------------------
1 | molecule man|Metro City| True| 2016-01-12 |{ "squad_name": "molecule man","hometown": "Uptown Hogwart","formed": "2016-01-12","active":false}

Now our main intention is to create a service that would allow us to search and query inside our members field. It means our main interest is the JSONField data where we want to do CRUD operation and should be able to search the property in json attribute(i.e. member) and get the data it holds. 

1. The root api should hold these information. The first link is for the all the attribute value that the database holds. The second one is for the value that the member field holds. 

GET /api/
{
    "superhero": "{url}/api/superhero/", 
    "members": "{url}/api/members/"
}

2.The below api should provide all the members data. 
	/api/members/

3. The below api should provide all the member data that belongs to primary key 24.
	/api/members/24/

4. The below api should give the list of member with primakry key whose members are active. This is just an example. We should be able to search member for other property values also. Like in this case squad_name, formed, hometown.  

/api/members/?active=true  => list members that holds active = true value.

5. Similarly, we should be able to Create Read Update & Delete on JSONField and also on superhero endpoint for entire table filed. 
   Things to ponder: if anybody want to change the other field in database they should be able to do through the json data column. 

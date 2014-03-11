import mwclient
site = mwclient.Site('wikieducator.org','/')

site.login(username,password) 
page = site.Pages['User:Akash_Agarwal/Prototypes/Eactivity']
fullpage=page.get_expanded()


lines=fullpage.splitlines();
i=0
activities={}
while i < len(lines):
	if (lines[i].find('|-')!=-1):
		i+=1
		t=lines[i].split('User:')
		try:
			user=t[1].split('|')[0]
		except:
			break
		i+=2
		t=lines[i].split('|[')
		blog=t[1].split(']')[0]
		try:
			activities[user].append(blog)
		except:
			activities[user]=[]
			activities[user].append(blog)
	i+=1


text=""

for i in activities:
	text+="*'''"+i+"'''  Number of activities:"+str(len(activities[i]))+"\n"
	for j in activities[i]:
		text+="**"+j+"\n"


page2 = site.Pages['User:Akash_Agarwal/Prototypes/EActivityStats']
page2.edit()
page2.save(text)

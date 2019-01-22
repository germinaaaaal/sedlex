import discord

client = discord.Client()

@client.event
async def on_ready():
	print("The bot is ready!")
	await client.change_presence(game=discord.Game(name=">help"))

charter = {
	"1" : "A resident is a nation that resides in Conifer. Residents shall be granted the following rights: \na. Freedom of speech, of peaceful association/assembly,\nb. Freedom from incriminating themselves and from being tried twice for the same crime,\nc. Right to being informed of requested Rulings involving them.\nd. Freedom from being incriminated due to ex post facto legislation or any attainder bill.\ne. Right to fair and reasonably fast hearing and judgement in any legal proceedings and to the presumption of innocence.\nf. Right to view the full text of any Motion that is being voted on or has passed in the Regional Council, and of the Second Charter of Conifer.",
	"1a" : "Freedom of speech, of peaceful association/assembly,",
	"1b" : "Freedom from incriminating themselves and from being tried twice for the same crime,",
	"1c" : "Right to being informed of requested Rulings involving them.",
	"1d" : "Freedom from being incriminated due to ex post facto legislation or any attainder bill.",
	"1e" : "Right to fair and reasonably fast hearing and judgement in any legal proceedings and to the presumption of innocence.",
	"1f" : "Right to view the full text of any Motion that is being voted on or has passed in the Regional Council, and of the Second Charter of Conifer.",
	"2" : "A voting state is a resident that has resided in Conifer for 42 days continuously, is a puppet of a disclosed World Assembly (WA) member, and has received approval for becoming a voting state from at least 3 officials.",
	"3" : "A member state is a resident that has resided in Conifer for 5 days continuously and that is a member of the WA.",
	"4" : "Officials are member states.",
	"5" : "The Founder is Vyutsk.",
	"6" : "The Premier is an elected official responsible for: 6a, 6b, 6c, 6d, 6e, 6f, 6g.",
	"6a" : "Voting on WA resolutions as Conifer’s WA Delegate,",
	"6b" : "Appointing officers in-game in a rightful manner,",
	"6c" : "Conducting any necessary regional intelligence,",
	"6d" : "Maintaining embassies and relations with other regions,",
	"6e" : "Appointing ambassadors to regions or organisations,",
	"6f" : "Managing any other issues regarding foreign affairs and regional security.",
	"6g" : "Assigning specific additional tasks to the Speaker and Chief of Culture if so necessary.",
	"7" : "The Speaker is an elected official responsible for: 7a, 7b, 7c.",
	"7a" : "Conducting core procedures of the Regional Council of Conifer,",
	"7b" : "Regulating all regional communications,",
	"7c" : "Recruiting for the region.",
	"8" : "The Chief of Culture is an elected official responsible for organising events, occasions and activities in Conifer and otherwise increasing user engagement.",
	"9" : "The Chancellor is an elected official responsible for conducting core procedures of the Central Court of Conifer, including issuing Rulings.",
	"10" : "The Shadow Premier is an official appointed by the Premier, tasked with assisting the Premier with their responsibilities, excluding those described in 6a and 6b.",
	"11" : "The Shadow Speaker is an official appointed by the Speaker, responsible for assisting the Speaker in their responsibilities.",
	"12" : "The Shadow Chief is an official appointed by the Chief of Culture, responsible for assisting the Chief of Culture in their responsibilities.",
	"13" : "The Regional Commissioner is an official appointed by the Chancellor, responsible for: 13a, 13b, 13c.",
	"13a" : "Maintaining regional data, statistics and judicial/legislative archives,",
	"13b" : "Conducting all elections,",
	"13c" : "Substituting for the Chancellor in their responsibilities if the Chancellor has a conflict of interest regarding a Ruling.",
	"14" : "The Regional Council is an institution with the exclusive right to pass Motions.",
	"15" : "A Motion is legislation submitted by a group of 2 Member States, that may be used as follows: 15a, 15b, 15c, 15d, 15e, 15f.",
	"15a" : "To amend or replace this Second Charter of Conifer,",
	"15b" : "To create rules or laws besides the Second Charter of Conifer, without over-ruling it,",
	"15c" : "To establish any new regional institutions or positions aside from officials,",
	"15d" : "To ratify treaties or enter inter-regional organisations or institutions,",
	"15e" : "To, with good intent, remove an official from their position.",
	"15f" : "To amend a 15b/15c Motion or repeal a 15b/15c/15d Motion.",
	"16" : "All Voting States and Member States shall have the right to vote ‘For’ or ‘Against’ a Motion, with 15a/15e Motions requiring ⅔ approval, and other motions requiring majority approval.",
	"17" : "15a Motions shall have a 7 day debate period with 1-2 debating events & a 7 day voting period, whilst all other Motions shall have a 3 day debate period with 1 debating event & a 5 day voting period.",
	"18" : "The Central Court is an institution with the exclusive right to issue Rulings.",
	"19" : "A Ruling is a decision regarding the legality of the following: 19a, 19b, 19c.",
	"19a" : "A 15b/15c/15d/15e Motion.",
	"19b" : "Actions of states.",
	"19c" : "Any hypothetical scenario.",
	"20" : "Any resident has the right to request a Ruling.",
	"21" : "A 19a Ruling may repeal the Motion in question or a part of said Motion.",
	"22" : "A 19b Ruling may involve consequences for the involved, including the following: 22a, 22b, 22c, 22d.",
	"22a" : "Ejection or a temporary or permanent ban from the region.",
	"22b" : "Blocking a state from using modes of communication in Conifer or from taking part in specific regional occasions temporarily or permanently.",
	"22c" : "Removing an official from their position.",
	"22d" : "Forcing any of the aforementioned consequences upon a repeat offence.",
	"23" : "A Premier election is organised every 4 months - in April, August and December.",
	"24" : "A Speaker election and Chief of Culture election are simultaneously organised 2 weeks after every Premier election.",
	"25" : "A Chancellor election is organised 2 months after every Premier election - in February, June and October.",
	"26" : "All elections shall have a 7 day period for candidacy announcements and a 7 day voting period.",
	"27" : "Only Member States may run for office, and they may do so unless they’ve been in the position for 8 months or longer continuously or if they’ve served in the position at some point in the last 4 months, but do not serve in the position.",
	"28" : "All Voting States and Member States are eligible to vote.",
	"29" : "A full preferential voting system shall be used for all elections, and a “look for other candidates” option shall be available to voters if there are less than 2 candidates.",
	"30" : "A State of Emergency is a special state where all Motions and the Second Charter of Conifer excluding 30. and 31. are no longer considered in force.",
	"31" : "A State of Emergency may be called by any official and may be cancelled by a group of 4 officials.",
	"32" : "Reg. 2. and 3., a state shall not lose their status of Voting State or Member State if they cease to exist or leave the region, but return within 3 days.",
	"33" : "Reg. 3., the Founder shall always be considered a Member State even if they don’t fulfill the requirements for being a Member State.",
	"34" : "Reg. 4., if an Official appoints another Official, they may also replace or fire this Official, though, to replace or fire the Regional Commissioner, approval from the Founder is required.",
	"35" : "Reg. 4., if an Official resigns or fails to fulfill the requirements for holding their role for over 3 days, their position shall be considered vacant unless otherwise specified in 36., 37., 38. or 39.",
	"36" : "Reg. 10., the Shadow Premier shall become the Premier pro tem if the Premier resigns or fails to fulfill the requirements for holding the role for over 3 days. If both positions become vacant, the Founder appoints a new Premier.",
	"37" : "Reg. 11., the Shadow Speaker shall become the Speaker pro tem if the Speaker resigns or fails to fulfill the requirements for holding the role for over 3 days. If both positions become vacant, the Founder appoints a new Speaker.",
	"38" : "Reg. 12., the Shadow Chief shall become the Chief of Culture pro tem if the Chief of Culture resigns or fails to fulfill the requirements for holding the role for over 3 days. If both positions become vacant, the Founder appoints a new Chief of Culture.",
	"39" : "Reg. 13., the Regional Commissioner shall become the Chancellor pro tem if the Chancellor resigns or fails to fulfill the requirements for holding the role for over 3 days. If both positions become vacant, the Founder appoints a new Chancellor.",
	"40" : "Reg. 13., for all intents and purposes, the Regional Commissioner shall be considered unaffiliated with and independent from any other official, except in the case of alleged election fraud involving the Regional Commissioner.",
	"41" : "Reg. 13b, these responsibilities shall be fulfilled by the Founder if the position of Regional Commissioner is vacant or the Regional Commissioner has a conflict of interest.",
	"42" : "Reg. 13c, these responsibilities shall be fulfilled by the Founder if both the Chancellor and the Regional Commissioner have a conflict of interest.",
	"43" : "Reg. 23., upon the election of a new Premier the position of Shadow Premier shall become vacant.",
	"44" : "Reg. 24., upon the election of a new Speaker the position of Shadow Speaker shall become vacant.",
	"45" : "Reg. 24., upon the election of a new Chief of Culture the position of Shadow Chief shall become vacant.",
	"46" : "Reg. 24., this election must also be held upon the passage of the Second Charter of Conifer.",
	"47" : "Reg. 29., if there are no candidates, the start of the voting period shall be delayed until a member state announces their candidacy.",
	"48" : "Reg. 29., if an election ends in a tie, the Founder shall break that tie.",
}

commands = {
	"help" : "List of commands: \n`>help`: list of commands \n`>charter [section number]`: quotes the Second Charter of Conifer \n`>define [term]` defines a term. \n\n`Sedlex by Athidill`",
	"define": "Known terms: `premier`, `commissioner`, `speaker`, `chief of culture`, `shadow`, `motion`, `charter`.\nUse `>define [term]`",
	"define premier" : "The Premier (§6) is the executive chief of Conifer. They are responsible for World Assembly affairs and the defense of the region, as well as directing government policy.",
	"define chancellor" : "The Chancellor (§9) directs judiciary affairs in the Conifer Central Court. They issue court Rulings.",
	"define commissioner" : "The Commissioner (§13) is responsible for organising elections. They are impartial and independent.",
	"define speaker" : "The Speaker (§7) is responsible for all communications in Conifer, as well as recruiting for the region.",
	"define chief of culture" : "The Chief of Culture (§8) directs cultural activity in Conifer such as artistic events and roleplay.",
	"define shadow" : "Shadow officers (§10, §11, §12) assist the Officers in their duties and may take their place in the event of the Officers not being able to serve their duties.",
	"define motion" : "Motions (§15) are bills proposed by Member States that create new laws with the Charter without interfering with it.",
	"define charter" : "The Charter of Conifer (Second Edition) is the essential text that establishes democracy and order in Conifer. It is the Constitution of the region.",
}

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content[0] == ">":
		if "help" in message.content:
			await client.send_message(message.channel, commands["help"])
		elif "define" in message.content:
			await client.send_message(message.channel, commands["define"])
		elif len(message.content.split(" ")) > 1:
			if message.content.split(" ")[0] in [">define", ">def", ">d"]:
				defined = "define " + message.content.split(" ")[1]
				await client.send_message(message.channel, "`" + commands[defined] + "`")
			elif message.content.split(" ")[0] in [">charter", ">c"]: 
				article = message.content.split(" ")[1]
				if article in charter:
					await client.send_message(message.channel, ("`Charter §%s: " + charter[article] + "`") % article) 
				else:
					await client.send_message(message.channel, "`Charter section not found.`")
		else:
			await client.send_message(message.channel, "`sorry, couldn't understand that.`")

client.run('NTM2NTc4MjczNzg2ODU1NDI0.DyZL8A.oo5B9VY2ru8WZKcQrZ6pS8Kj_kg')
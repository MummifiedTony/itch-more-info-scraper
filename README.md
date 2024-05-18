# itch-more-info-scraper
Scrape or scan the more details of an item on Itch and output to a JSON file

Think of this as a Pt.2 to my last repo that was made. https://github.com/MummifiedTony/itch-bundle-item-URL-puller

This is the continuation of my goal to make a better Itch item library. The first part was about looking at all the bundles you or I have bought on Itch.io and grabbing the URLs of every item, eliminating duplicates, and then putting them to a txt file. After I was done with that, made a quick code that scanned all the additional details that could be found on all the items, and then dumped them into a txt file.

Those details were, Links, Status, Code license, Release date, Authors, Multiplayer, Author, Platforms, Languages, Asset license, Genre, Inputs, Mentions, Rating, Category, Tags, Player count, Average session, Made with, Updated, Published, Accessibility, and Publisher. I didn't feel like posting the code that got me here so I skipped it.

The code used here in this repo goes into the table that is present on every item and looks at the details and points to each spot that needs to be copied over. It also pulls the name of the item from the url rather than what the name for the item might be on the page for the item. So that is one aspect of this code that I think could be a little better. It was getting late and I just wanted it to be done. And once it has gathered everything from the list it exports to a JSON file. Mostly because I plan on using this data to make my own search function in another app/program/site/thing.

One other important thing is that this was made with the help of ChatGPT. If there is something off or wrong with the code feel free to let me know.

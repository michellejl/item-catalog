from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item

engine = create_engine('sqlite:///categoryitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

################### CATEGORY 1: Development Tools ###################
category1 = Category(name="Development Tools")
session.add(category1)
session.commit()

item1 = Item(
  name = "iTerm2",
  description = "iTerm2 is a replacement for Terminal on Mac and the successor to iTerm. iTerm2 brings the terminal into the modern age with features you never knew you always wanted.",
  image_url = "iterm.png",
  website = "https://www.iterm2.com/",
  category = category1
)
session.add(item1)
session.commit()

item2 = Item(
  name = "Hyper",
  description = "A Terminal replacement app with a goal to create a beautiful and extensible experience for command-line interface users, built on open web standards.",
  image_url = "none.png",
  website = "https://hyper.is/",  
  category = category1
)
session.add(item2)
session.commit()

item3 = Item(
  name = "Powershell",
  description = "PowerShell Core is a cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework that works well with your existing tools and is optimized for dealing with structured data (e.g. JSON, CSV, XML, etc.), REST APIs, and object models. It includes a command-line shell, an associated scripting language and a framework for processing cmdlets.",
  image_url = "powershell.png",
  website = "https://docs.microsoft.com/en-us/powershell/",
  category = category1
)
session.add(item3)
session.commit()

item4 = Item(
  name = "CodeKit",
  description = "CodeKit automatically compiles all those awesome languages you read about in tutorials.",
  image_url = "codekit.png",
  website = "https://codekitapp.com/",
  category = category1
)
session.add(item4)
session.commit()

item5 = Item(
  name = "GitKraken",
  description = "The legendary Git GUI client for Windows, Mac and Linux. GitKraken now offers Git novices and pros a consistent experience across Mac, Windows and Linux. And makes Git operations not only performant and efficient, but understandable, visual, and perhaps even just a little bit…fun!",
  image_url = "gitkraken.png",
  website = "https://www.gitkraken.com/",
  category = category1
)
session.add(item5)
session.commit()

item6 = Item(
  name = "Sequel Pro",
  description = "Sequel Pro is a fast, easy-to-use Mac database management application for working with MySQL databases.",
  image_url = "sequelpro.jpg",
  website = "https://www.sequelpro.com/",
  category = category1
)
session.add(item6)
session.commit()

item7 = Item(
  name = "Virtual Box",
  description = "VirtualBox is a general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use.",
  image_url = "virtualbox.png",
  website = "https://www.virtualbox.org/",
  category = category1
)
session.add(item7)
session.commit()

item8 = Item(
  name = "Transmit",
  description = "The gold standard of macOS file transfer apps just drove into the future. Transmit 5 is here. Upload, download, and manage files on tons of servers with an easy, familiar, and powerful UI. It’s quite good.",
  image_url = "transmit.png",
  website = "https://panic.com/transmit/",
  category = category1
)
session.add(item8)
session.commit()

################### CATEGORY 2: IDE's and Text Editors ##############
category2 = Category(name="IDE's and Text Editors")

item9 = Item(
  name = "Visual Studio Code",
  description = "Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and Unity).",
  image_url = "vscode.png",
  website = "https://code.visualstudio.com/",
  category = category2
)
session.add(item9)
session.commit()

item10 = Item(
  name = "Atom",
  description = "Atom is a text editor that's modern, approachable, yet hackable to the core—a tool you can customize to do anything but also use productively without ever touching a config file.",
  image_url = "atom.png",
  website = "https://atom.io/",
  category = category2
)
session.add(item10)
session.commit()

item11 = Item(
  name = "PyCharm",
  description = "PyCharm is a Python IDE for Professional Developers created by JetBrains. PyCharm knows everything about your code. Rely on it for intelligent code completion, on-the-fly error checking and quick-fixes, easy project navigation, and much more.",
  image_url = "pycharm.png",
  website = "https://www.jetbrains.com/pycharm/",
  category = category3
)
session.add(item11)
session.commit()

item12 = Item(
  name = "WebStorm",
  description = "Use the full power of the modern JavaScript ecosystem – WebStorm’s got you covered! Enjoy the intelligent code completion, on-the-fly error detection, powerful navigation and refactoring for JavaScript, TypeScript, stylesheet languages, and the most popular frameworks.",
  image_url = "webstorm.png",
  website = "https://www.jetbrains.com/webstorm/",
  category = category2
)
session.add(item12)
session.commit()


################### CATEGORY 3: Productivity Tools #################
category3 = Category(name="Productivity Tools")

item13 = Item(
  name = "Alfred",
  description = "Alfred is an award-winning app for Mac OS X which boosts your efficiency with hotkeys, keywords, text expansion and more. Search your Mac and the web, and be more productive with custom actions to control your Mac.",
  image_url = "alfred.png",
  website = "https://www.alfredapp.com/",
  category = category3
)
session.add(item13)
session.commit()

item14 = Item(
  name = "aText",
  description = "aText accelerates your typing by replacing abbreviations with frequently used phrases you define.",
  image_url = "atext.jpg",
  website = "https://www.trankynam.com/atext/",
  category = category3
)
session.add(item14)
session.commit()

item15 = Item(
  name = "1Password",
  description = "1Password remembers all your passwords for you. Save your passwords and log in to sites with a single click. It's that simple.",
  image_url = "1password.png",
  website = "https://1password.com/",
  category = category3
)
session.add(item15)
session.commit()

item16 = Item(
  name = "Bartender",
  description = "Bartender 3 lets you organize your menu bar apps, by hiding them, rearranging them, or moving them to the Bartender Bar. You can display the full menu bar, set options to have menu bar items show in the menu bar when they have updated, or have them visible in the Bartender Bar.",
  image_url = "bartender.jpg",
  website = "https://www.macbartender.com/",
  category = category3
)
session.add(item16)
session.commit()

item17 = Item(
  name = "Freeter",
  description = "Freeter is a productivity app that allows you to gather everything you need to work in one place and access them quickly and easily.",
  image_url = "freeter.png",
  website = "https://freeter.io/",
  category = category3
)
session.add(item17)
session.commit()

item18 = Item(
  name = "LICEcap",
  description = "LICEcap can capture an area of your desktop and save it directly to .GIF (for viewing in web browsers, etc) or .LCF (own native lossless format). LICEcap is an intuitive but flexible application (for Windows and now OSX), that is designed to be lightweight and function with high performance.",
  image_url = "licecap.png",
  website = "https://www.cockos.com/licecap/",
  category = category3
)
session.add(item18)
session.commit()

item19 = Item(
  name = "Spectacle",
  description = "Spectacle allows you to organize your windows without using a mouse. Spectacle makes use of several keyboard shortcuts that trigger specific window actions. A window action is nothing more than a command that tells Spectacle how to change the size and/or position of a particular window.",
  image_url = "spectacle.png",
  website = "https://www.spectacleapp.com/",
  category = category3
)
session.add(item19)
session.commit()

item20 = Item(
  name = "Snippets Lab",
  description = "Be more productive with SnippetsLab. SnippetsLab is an easy-to-use code snippets manager. It helps you to collect and organize valuable code snippets and makes sure that you have easy access to them whenever you want.",
  image_url = "snippetslab.png",
  website = "https://www.renfei.org/snippets-lab/",
  category = category3
)
session.add(item20)
session.commit()


################### CATEGORY 4: Documents ##########################
category4 = Category(name="Documents")

item21 = Item(
  name = "Evernote",
  description = "Capture, organize, and share notes from anywhere. Your best ideas are always with you and always in sync.",
  image_url = "evernote.png",
  website = "https://evernote.com/",
  category = category4
)
session.add(item21)
session.commit()

item22 = Item(
  name = "Marked 2",
  description = "Marked is a previewer for Markdown files. Use it with your favorite text editor and it updates every time you save. With robust features for previewing, reviewing and exporting beautiful documents, you can work in plain text while reveling in rich formatting.",
  image_url = "marked.png",
  website = "http://marked2app.com/",
  category = category4
)
session.add(item22)
session.commit()

item23 = Item(
  name = "Total Finder",
  description = "TotalFinder works like the normal Finder but adds tabs, dual panel, colored labels and other features.",
  image_url = "totalfinder.png",
  website = "https://totalfinder.binaryage.com/",
  category = category4
)
session.add(item23)
session.commit()

item24 = Item(
  name = "OneDrive",
  description = "Get to your files and photos from anywhere, on any device. Share and work together with anyone in your work and life.",
  image_url = "onedrive.png",
  website = "https://onedrive.live.com/about/en-us/",
  category = category4
)
session.add(item24)
session.commit()

item25 = Item(
  name = "Calibre",
  description = "calibre is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts. ",
  image_url = "calibre.png",
  website = "https://calibre-ebook.com/download",
  category = category4
)
session.add(item25)
session.commit()


################### CATEGORY 5: Graphics and Photo Editors #########
category5 = Category(name="Graphics and Photo Editors")

item26 = Item(
  name = "Sketch",
  description = "Sketch is a design toolkit built to help you create your best work — from your earliest ideas, through to final artwork.",
  image_url = "sktech.jpg",
  website = "https://www.sketchapp.com/",
  category = category5
)
session.add(item26)
session.commit()

item27 = Item(
  name = "Affinity Photo",
  description = "Faster, smoother and more powerful than ever, Affinity Photo continues to push the boundaries for professional photo editing software. With a huge toolset specifically engineered for creative and photography professionals, whether you are editing and retouching images, or creating full-blown multi-layered compositions, it has all the power and performance you will ever need.",
  image_url = "affinityphoto.png",
  website = "https://affinity.serif.com/en-us/photo/",
  category = category5
)
session.add(item27)
session.commit()


################### CATEGORY 6: Date and Do Things Trackers ########
category6 = Category(name="Date and Do Things Trackers")

item28 = Item(
  name = "2Do",
  description = "2Do’s simplistic appearance is only skin deep. It can be a simple to-do list, helping you in staying on top of your daily chores, or a full-featured GTD tool for heavy taskers. It houses an incredibly powerful productivity-aware engine, and can be as fierce as your workflow.",
  image_url = "2do.png",
  website = "https://www.2doapp.com/",
  category = category6
)
session.add(item28)
session.commit()

item29 = Item(
  name = "Google Calendar",
  description = "The new Google Calendar app helps you spend less time managing your schedule and more time enjoying it.",
  image_url = "googlecalander.png",
  website = "https://www.google.com/calendar",
  category = category6
)
session.add(item29)
session.commit()

################### CATEGORY 7: Communication ######################
category7 = Category(name="Communication")

item30 = Item(
  name = "Franz",
  description = "Franz is your messaging app for WhatsApp, Facebook Messenger, Slack, HipChat, Telegram and many many more.",
  image_url = "franz.png",
  website = "https://meetfranz.com/",
  category = category7
)
session.add(item30)
session.commit()

item31 = Item(
  name = "Spark",
  description = "Email has taken too much time from people. Spark gives time back to all those who live by their inbox. Quickly see what's important and clean up the rest.",
  image_url = "spark.jpg",
  website = "https://sparkmailapp.com/",
  category = category7
)
session.add(item31)
session.commit()

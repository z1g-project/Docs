# Introduction

Welcome to the tutorial: How to Create Apps on Terbium

## Step 0. (Post Addon)

First Chose if its a Web App or System App (Local)

### Whats a Web App?

A Web App is a Application that isn't stored localy and is a website. Ill Explain Later the specific tag you need to add. **HOWEVER** If your app doesn't need to be Proxied then you can add the tag ill mention later to the Launcher Code.

### Whats a System App

A System App is a Local Application that is in the Directory of the `/static` It does not run off a Proxy or Normal Website and has a special tag you need to use.

## Step 1. Setting Up the App

To get Started navigate to `/static/index.html` Once you are there Customize the code below and insert it into somewhere in the ``appsDesk`` Class Which can be located from Line 97 to Line 271. However now you need to know if you have an Icon Setup You can use either the **SVG** or **IMG** Versions of the Code Which Are Listed Below:

Image Version:
`<div class="deskapp" title="Example" onclick="new WIN('(link)[https://docs.z1g-project.repl.co/services/terbium]', '(icn)[./resources/terbium.png]', '(title)[Example Application]', '(os)[true]', '(full)[false]', '(appname)[examples]');">
                        <img src="./resources/terbium.png" id="example" title="examples" class="appIcon">
                    </div>`

SVG Version:
`<div class="deskapp" title="example" onclick="new WIN('(link)[https://docs.z1g-project.repl.co/services/terbium]', '(icn)[./resources/example.svg]', '(title)[example]', '(os)[true]', '(full)[false]', '(appname)[example]');">
                        <svg class="appIcon" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path class="fill" d="M25.84 33.44H18.32V55H11.08V33.44H3.56V26.64H25.84V33.44ZM39.4784 36.36L44.4384 26.68H52.7584L44.8384 40.88L52.7584 55H44.4384L39.4784 45.36L34.6384 55H26.2784L34.2384 40.88L26.2784 26.68H34.6384L39.4784 36.36ZM75.4884 33.44H67.9684V55H60.7284V33.44H53.2084V26.64H75.4884V33.44Z"/>
                        </svg>
                    </div>`

Now that you have selected which version your gonna use follow the next steps to learn about what the tags mean

## Step 2. Tags

So as im sure you know there are a ton of tags as seen so here is a markdown of all the tags in the App's Dock Configuration

#### (link) Tag

The Link Tag is used to define the URL or Endpoint of your application. If this is local set it up with `./point of local app here` If not then skip that and set it up with your url endpoint for Example: `https://google.com/`

#### (icn) Tag

The Icon Tag is used to define the Icon the Application will use however it is bugged right now. I suggest storing the icon in `static/resources` to reduce loading times and server latency!

**NOTE If your icon isn't working on a OS app then it might not work because Terbium is finicky I am in contact with SNOOT (the dev) to Work on this

#### (title) tag

The Title Tag is used to define the Title of the Window. This can Include Spaces and will be used.

#### (os) tag

The OS Tag is used to define wiether the App will be Proxied or not. **THIS IS VERY IMPORTANT DO NOT SKIP OVER THIS** Once you have chosen wiether the app is OS'ed or not make sure that your version of Terbium supports it. If your using [Terbium Cloud](https://github.com/z1g-project/terbium-cloud) For **ALL** Apps, Regardless of wiether you want it proxied or not must be set to `true` and you can configure the Proxy Settings with the URL Tag. If your using normal Terbium your good just select true or false depending on the circum stance

#### (full) tag

The full tag is mostly unused and won't be necesary for usage but its basicly an experiemntal fullscreen option. 

#### (appname) tag

The appname tag is used to define the app config in `./js/windows.js` This must be the same as the name used in the Windows.Js. This also configures the ?app= command for quick launch

## Step 3. Adding the App to Windows.JS

First Navigate to ./js/windows.js and navigate to line: _blank
Then Modify the code below:
`stuff here`

## Step 4. Other Configuration Settings

Work in progress!
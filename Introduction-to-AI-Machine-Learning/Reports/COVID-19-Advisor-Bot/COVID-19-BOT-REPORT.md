## Report: Building a COVID-19 Advisor Bot using Azure

- ##### Use Case Scenario

  The situation with the COVID-19 pandemic has caused a lot of disinformation and fake news to appear on the Internet. People have trouble with getting the information they require from reliable sources, so the bot was created to provide accurate data and get early advice regarding COVID-19 symptoms. The Bot will help with basic information about the COVID-19 pandemic, tests, symptoms and actions which should be taken in case of an infection. Additionally, the Bot will present current statistics in Poland and can help assess the risk of an infection with a quick survey on the symptoms and points of contact. 

  

- ##### Steps taken to build the Bot

  The Bot was designed in the Bot Framework Composer, with additional Azure resources applied whenever needed. In order to create a fully working bot from this repository, the following steps should be taken:

  

  - Download and install the Azure Bot Framework Composer (the Bot composer is an open-source app which allows bots creation using a graphical interface). The prerequisites to install the Bot Framework Composer are the Bot framework Emulator and .NET Core SDK 3.1 and above.

    https://docs.microsoft.com/en-us/composer/install-composer

    ![image-20201113202351620](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113202351620.png)

    *Appearance of the Bot Framework Composer v1.1.1*

    

  - Go to the Azure portal login and create a new resource Group. 

    https://portal.azure.com/

    ![image-20201113202916000](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113202916000.png)

    *Creating a new resource group in the Azure Portal view.*

    

  - Create a new Language Understanding Service and connect it to the Bot project in the Bot Framework Composer.

    ![image-20201113202948592](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113202948592.png)

    *Creating a new LUIS instance (important note: In Composer V1.1.1, LUIS works correctly only when the instance is created in the West US region).*

    

    ![image-20201113203353884](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113203353884.png)

    *Linking the correct configuration for the newly created LUIS instance (Go to Azure Bot Framework Settings -> Bot Settings and copy the parameters from the Keys and Endpoint tab on the Azure portal)*

    

  - Create a QnA instance and fill the database with frequently asked questions. Go to https://www.qnamaker.ai/ and follow the steps listed to create a personalized QnA database.

    ![image-20201113203803134](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113203803134.png)

    *View of the QnA Maker*

    

    ![image-20201113204313754](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113204313754.png)

    *Creating a new instance of QnA*

     

    ![image-20201113204449898](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113204449898.png)

    *Creating a link to the created instance in the Bot Framework Composer (Settings -> Bot Settings and copy parameters)*

    

  - If you would like to host an Azure Function gathering data about the current COVID-19 statistics locally, download Visual Studio Code and install the Azure Functions plugin. 

    ![image-20201113204915432](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113204915432.png)

    

    Azure Functions Core Tools, which allow to run Functions locally without deployment, can also be downloaded and installed:

    https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash

    

    Run a Python function from the repository using the following command:

    `func start HttpTriggerGetCases`

    ![image-20201113205211951](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113205211951.png)

    

  - Launch the Bot locally using the Bot Framework Composer: In the top right corner, click the Start Bot button and select Test in Emulator. The whole solution can also be deployed to the Azure cloud if you would not like to host it locally. 

    

    ![image-20201113205446345](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113205446345.png)

    ![image-20201113205645423](C:\Users\Jakub\AppData\Roaming\Typora\typora-user-images\image-20201113205645423.png)

  

- ##### Architecture

  The main part of the Bot design was done in the Bot Framework Composer. The Bot also uses additional Azure services:

  

  - Language Understanding (LUIS)

    https://www.luis.ai/

  - QnA Maker

    https://azure.microsoft.com/pl-pl/services/cognitive-services/qna-maker/

  - Azure Functions

    https://azure.microsoft.com/en-us/services/functions/

    

    

  Architecture diagram:

  ![diagram](C:\Users\Jakub\Downloads\diagram.png)
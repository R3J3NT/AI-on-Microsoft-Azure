## Report: Bird Species Cataloging system using Azure Custom Vision

Video Presentation: 



- ##### Use Case Scenario

  One of the most time-consuming parts of taking photos of nature, especially bird photos, is analyzing and cataloging them after a whole day of shooting. This system can automate the whole process, recognize bird species and catalog them into correct folders without much human action. The only thing which the human needs to do is to copy photos for verification from an SD card to the photos folder and run the script - the images will be transferred to the correct place.

  

- ##### Steps taken to build the System

  The system was built using Azure Custom Vision and Python script which executes the cataloging function. Custom Vision was trained on four species of birds and the model was published to be accessible as an API. The Python script generates the correct catalogs, calls Custom Vision API with images and transfers photos to correct catalogs according to the response from Azure.

  

  - Log in to the Azure portal https://portal.azure.com/, and create a new resource group for this project.

    ![1-Resource-Group.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/1-Resource-Group.PNG)

    

  - From the portal, create a new Cognitive Service Custom Vision resource. It should contain both Training and Prediction resources. The Python script is prepared to use the Free F0 tier, with maximum 2 transactions per second.

    ![2-Create-Resources.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/2-Create-Resources.PNG)

    

  - Go to the Custom Vision Portal https://www.customvision.ai/, and log in.

    ![3-Custom-Vision-Portal.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/3-Custom-Vision-Portal.PNG)

  

  - Create a new project using the resources from point 2. The project should be Classification type and use Multiclass (Single tag per image).

    ![4-Create-Project.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/4-Create-Project.PNG)

    

  - After creating the new project, go to Add images.

    ![5-Add-images.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/5-Add-images.PNG)

    

  - Load all of your training photos and add correct labels for them.

    ![6-Label.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/6-Label.PNG)

    

  - Start training your model using the Train button.

    ![7-Train-Model-Start.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/7-Train-Model-Start.PNG)

    

  - After some time, you will receive a summary of your model training.

    ![8-Train-Summary.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/8-Train-Summary.PNG)

    

  - You can test your model using the Quick test button on the portal and, if the results are accurate enough, you can publish your model to be accessible from API. To do this, you should click the Publish button.

    ![9-Publish.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/9-Publish.PNG)

    

  - After publishing, you need to copy your connection parameters (Endpoint and Prediction-Key) from the Prediction URL tab. Once you have your parameters, you need to set them to environmental variables with keys: "SUBSCRIPTION_KEY" and "ENDPOINT" to be accessible from the Python script.

    ![10-Get-parameters.PNG](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/10-Get-parameters.PNG)

    

  

- ##### Architecture

  Python script calling the Azure Custom Vision API where the trained model is published.

  https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/

  

  Architecture diagram:

  ![11-Architecture.png](https://github.com/R3J3NT/AI-on-Microsoft-Azure/blob/main/Introduction-to-AI-Machine-Learning/Reports/Bird-Spieces-Cataloging/images/11-Architecture.png)

  
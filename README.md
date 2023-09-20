# LLM_Tools
<br>
<strong>chat_API_gui</strong>
<br>
<br>

<img src="https://github.com/AlphaLoris/LLM_Tools/blob/master/resources/Chat_Completion_AI_UI.jpg" alt="Prompt Tab" align="middle" width="700"/>


<br>
This application provides a graphical user interface for the OpenAI chat completion API.  It allows you to choose one of their Large Language Models to interact with, provide values for all of the parameters that control the behavior of the LLM, build a prompt for the LLM, submit it, and then review the LLM's response. Here is a brief description of its features/behavior:

Prompt tab (above) - The tab where you can provide your API key, choose the model you want to submit your prompt to, set the behavioral parameters for the model, and define your prompt.
<br>
- API Key - Prompts you for an OpenAI API key, then saved the value you provide in your operating system's keychain. You can also edit the API key should it change (how to get an API key is described below).
- Model Drop-Down Menu - After you have provided an API key, this menu is dynamically populated based on the models your API key has access to. Basically the application runs through the list of models that support the chat completion api and sends an api call to the api using each of the models. If the API call succeeds, the model is added to the dropdown menu. This is done each time you start the application.
- Parameters - These parameters control the model's behavior. If you hover your cursor over the name of the parameter, the application will display a brief description of the purpose of the parameter The "Restore Defaults" button will reset them to their original values, which I selected to provide predictable responses to prompts.
- Context length - this is the context window/length size for the model you have selected in tokens. A token is all or a portion of a word, so the number of tokens in a prompt will be maybe 25% larger than the number of words. The context window size determines the maximum number of tokens the interaction will be composed of.  Both the prompt and the response must fit into the context window.  That means that if you have a 4096 token contenxt window and you use 3000 tokens in the prompt, the LLM will limit the maximum length of its response to 1096 tokens.
- Current token count - this is the number of tokens included in all of the message components of your prompt as will as 3 or 4 tokens for the additonal elements the API adds to the prompt to frame it properly for the LLM.  The application will check the length of your prompt before submitting it to the API, and if it exceeds the context window, will alert you and not submit the prompt.
- Add message component button - This button creates and allows you to edit a prompt message component.  Prompts can consist of one or of many message components.  There is an introduction to the use of these components and the associated roles on the Guide to Prompt Structure tab. There are also links to prompting resources on that tab.
- Submit prompt button - This button submits the prompt you have written to the LLM. When the LLM responds, the attributes of the response will be displayed below the message components, and the text of response will be displayed on the "Response" tab.
- Delete prompt button - this button deletes your message components and the LLM response from the previous prompt so that you can build your next prompt.
- Message component role drop-down menu - this menu allows you to assign a role (system, user, assistant) to your message component.  The purpose of these roles is discussed briefly on the Guide to Prompt Structure tab of the application.
- Message component text - This text displays the first few words of the message component so you can remember what the message component says.
- Up and down arrows - these arrows allow you to move the corresponding message component up or down in the list of message components.
- Edit button - opens the message component window so you can edit the component if you need to.
- Reponse ID - This is the ID the API assigns the model's response.
- Response created on - this is the time and date the response was created in cryptic programmer code. I don't know how to read it.
- Usage - shows the number of tokens used by the prompt and the model's response(s), and the total number of tokens used. These numbers are used to calculate the charge for the interaction.
- Completion tokens - the number of tokens used in the Model's response to your prompt.
- Prompt tokens - the number of tokens in the prompt.
- Total tokens - The total number of tokens used in the turn; the sum of the number of Completion tokens and Prompt tokens.
- Finish Reasons - The reason the model stopped generating the response. Unless you specified a stop text string in the parameters, the Finish Reason will generally be "Stop" which I understand to mean that the model decided it had reached the end of the response. If the API call fails, you will see a description of that here.
<br>
Response tab - The tab where the text of the model's response to your prompt will be displayed.
<br>
<br>
<img src="https://github.com/AlphaLoris/LLM_Tools/blob/master/resources/Chat_Completion_AI_UI_2.jpg" alt="Prompt Tab" align="middle" width="700"/>


<br>
<br>
Guide to Prompt Structure tab - this tab provides some brief guidance to prompting, and links to some other prompting resources.
<br>
<br>


<img src="https://github.com/AlphaLoris/LLM_Tools/blob/master/resources/Chat_Completion_AI_UI_3.jpg" alt="Prompt Tab" align="middle" width="700"/>

<br>
API Key - In order to use this application, you will need an OpenAI API key. You can get one by creating an account at OpenAI.com and associating a credit card with your account.  Each API call cost a few cents at most.
<br>
<br>
<br>
<strong>Prompt_tester</strong>
<br>
<br>
This tool is an extension of the chat_gui application that allows the user to to run batch testing of a prompt. It allows the user to define a prompt template in its Prompt tab that asks the model to perform an operation on the included content, and directs the model to respond with a JSON. It also allows the user to identify an output directory and a file containing the target JSON schema for the output. When executed it iterates through a source directory of .txt files and embeds the contents of each file in the prompt template by replacing the "--{?}--" string in the prompt template with the file contents.  The completed prompt is then submitted to the LLM and the response is parsed to remove any content before or after the JSON.  The JSON is then validated against the JSON schema. Finally, the result of the validation and the output JSON are written to the output directory.
<br>
<br>
<img src="https://github.com/AlphaLoris/LLM_Tools/blob/master/resources/Prompt_Tester.jpg" alt="Prompt Tab" align="middle" width="700"/>
<br>
<br>
<strong>Token_counter</strong>
<br>
<br>
<br>
This tool provides a gui for ticktoken that allows the user to paste a block of text into the text window, and then use the controls to count the tokens in the text.

<img src="https://github.com/AlphaLoris/LLM_Tools/blob/master/resources/token_counter.jpg" alt="Prompt Tab" align="middle" width="700"/>
<br>
<br>

<strong>Text_splitter</strong>
<br>
<br>
This tool allows the user to browse to a directory containing a .txt file, and select the file. Text_splitter will then split the text file into chunks with the maximum size in tokens specified by the max_tokens value in the code. The max_token value is currently set to 4000 tokens.

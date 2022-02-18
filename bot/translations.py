
class Messages:

    START_MSG = "Hi there {}.\n\nI'm Youtube Uploader Bot.You can use me to upload any telegram video to youtube once you authorise me.You can know more from /help.\n\nThank you. 😇ඔබගේ ඕනෑම ගැටලුවක් @dasuking [DEVELOPER] මා වෙත යොමු කරන්න😇"

    HELP_MSG = [
        ".",
        "Hi there.\n\nFirst things first. You should be aware that youtube processes each and every video uploaded, and its AI is amazing that it flags the video for copyrights if it finds copywrited content as soon as its uploaded, and you will not be able to publish the video.\n\nRead through all the pages to know how I work.",

        "**Lets learn how I work.**\n\n**Step 1:** __You authorise me to upload to your youtube channel.More about this in comming pages.__\n\n**Step 2:** __You forward any Telegram video to me.__\n\n**Step 3:** __You reply __/upload __to the forwarded video file.You can also specify some title in the upload command, but its optional though.Title will follow the __`/upload`.__If no title is given, filename will be used as title.__\n\n**Step 4:** __I remotely download the file and uploads to your Youtube channel.__\n\n**Step 5:** __I send you the Youtube link after upload.__",

        "**Create your youtube channel**\n\nThere is no point in using me if you dont have a Youtube Channel.So go through the given steps to create one.\n\n**Step 1:** __Sign in to YouTube on a computer or using the mobile.__\n\n**Step 2:** __Try any action that requires a channel, such as uploading a video, posting a comment, or creating a playlist.__\n\n**Step 3:** __If you don't yet have a channel, you'll see a prompt to create a channel.__\n\n**Step 4:** __Check the details and confirm to create your new channel.__",

        "**Verify your YouTube account**\n\nYoutube take spam and abuse very seriously. So you are asked to verify your Youtube account. Once you've verified your account, you will be able to upload videos longer than 15 minutes. If you haven't verified your account every video uploaded which are longer than 15 minutes will be removed.\n[Verify your Youtube account here.](http://www.youtube.com/verify)\n\n__Remember to verify your project, else your uploads will be kept private.__",

        "**Now lets authorise.**\n\nYou need to give me the access to upload videos to your Youtube account.For that open the given link and allow access and copy the code. Come back here and type `/authorise copied-code` and send it.\n\n**Fear not!**\nI'm not a hacker or someone who wants to creep into people's privacy. I respect one's privacy. I'm here just to help anyone who wants help. If I was a hacker I won't be sitting here writing Telegram Bots."
    ]

    NOT_A_REPLY_MSG = "Please reply to some video file [කරුණාකර ගොනුවක් වෙත පිළිතුරු ලියන්න]."

    NOT_A_MEDIA_MSG = "No media file found [ගොනුවක් හඳුනා ගත නොහැකි විය]. "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media [මෙම ගොනුව වලංගු නොවේ]"
    
    DAILY_QOUTA_REACHED = "Looks like you are trying to upload more than 6 videos today! By default youtube only allows about 6 uploads daily, so this request might fail!! 😇දිනකට උඩුගත කළ හැකි වීඩියෝ ප්‍රමාණය උපරිම 06ක් වන අතර ඔබට ඊට වැඩි වීඩියෝ ප්‍රමාණයක් උඩුගත කිරීමට අවශ්‍ය නම් @dasuking අමතන්න😴"

    PROCESSING = "Processing..... [⚡Powered by @dasuking webserver⚡]"

    NOT_AUTHENTICATED_MSG = "You have not authenticated me to upload video to any account ⚡උඩුගත කිරීමට ඔබගේ ගිණුම තවමත් තහවුරු කර නොමැත😔. see /help to authenticate"

    NO_AUTH_CODE_MSG = "There is no code. Please provide some code ⚡වලංගු ආදනයන් ලබා දෙන්න😴"

    AUTH_SUCCESS_MSG = "Congrats, you have successfully authenticated me to upload to Youtube 🤹සාර්ථකව තහවූරු කරන ලදී😴.\nHappy uploading....!"

    AUTH_FAILED_MSG = "Authentication failed\nDetails:{}"
    
    AUTH_DATA_SAVE_SUCCESS = "Successfully saved the given auth data![සාර්ථකව ඔබගේ ගිණුම් තොරතුරු ලියාපදිංචි කරන ලදී]"
    

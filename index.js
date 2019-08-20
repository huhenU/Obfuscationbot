const botconfig = require("./botconfig.json");
const languaged = require("./languages.json");
const Discord = require("discord.js");
const YandexTranslator = require('yandex.translate');
var translator = new YandexTranslator("yandex-token-here");
const bot = new Discord.Client({disableEveryone: true});
bot.commands = new Discord.Collection();

bot.on("ready", async () => {
  console.log(`${bot.user.username} is now ready!`);

  bot.user.setActivity("the obfuscation channel", {type: "WATCHING"});

});

bot.on("message", async message => {;

  if(message.author.bot) return;

  if(message.channel.id == botconfig.helpchannel) {

    var l1 = Math.floor((Math.random() * 93) + 1);
    var l2 = Math.floor((Math.random() * 93) + 1);
    var l3 = Math.floor((Math.random() * 93) + 1);
    var l4 = Math.floor((Math.random() * 93) + 1);
    var l5 = Math.floor((Math.random() * 93) + 1);

  var func1 =
      translator.translate(message.content, `${languaged[l1]}`);



      var res;
      func1.then(function(result){
        res = result
    var func2 = translator.translate(res, `${languaged[l2]}`);
    func2.then(function(result2){
      res2 = result2
      var func3 = translator.translate(res2, `${languaged[l3]}`);
      func3.then(function(result3){
        res3 = result3
        var func4 = translator.translate(res3, `${languaged[l4]}`);
        func4.then(function(result4){
          res4 = result4
          var func5 = translator.translate(res4, `${languaged[l5]}`);
          func5.then(function(result5){
            res5 = result5
            var func6 = translator.translate(res5, 'en');
          func6.then(function(result6){
            res6 = result6
            message.channel.send(res6)
          })
          })
        })
      })

    })
});


};


});

bot.login(botconfig.token);

var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    if (d.getMinutes() < 10){
      m = "0" + d.getMinutes()
    }
    else {
      m = d.getMinutes()
    }
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})

var Fake = [
  'hey guys its me iul nedyr i get 10 hours of sleep each day<br>The howitzer (/ˈhaʊ.ɪtsər/) is an artillery weapon that falls between a cannon (or field gun) and a mortar. It is capable of both low angle fire like a field gun and high angle fire like a mortar, given the distinction between low and high angle fire breaks at 45 degrees or 1600 mils (NATO). With their long-range capabilities, howitzers can be used to great effect in a battery formation with other artillery pieces, such as long-barreled guns, mortars, and rocket artillery.<br>The term "howitzer" originated from the Czech word houfnice, meaning "crowd", which was later adapted into various European languages. Developed in the late 16th century as a medium-trajectory weapon for siege warfare, howitzers were valued for their ability to fire explosive shells and incendiary materials into fortifications. Unlike mortars, which had fixed firing angles, howitzers could be fired at various angles, providing greater flexibility in combat.<br>bye CHENG',
  'cheng<br>what is ur preferred steak doneness<br>CHENG',
  'asfvc CHENG',
  'Farenheit 415<br>CHENG',
  'Alan walker or CHENG',
  'over over CHENG',
  'ricegum or allen walker CHENG']

function fakeMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  $('<div class="message loading new"><figure class="avatar"><img src="https://cdn.discordapp.com/attachments/875254905554755678/1330781350680199169/20240509_144804_HDR.jpg?ex=678f3a36&is=678de8b6&hm=784754ffda8bb3668a03bd0cff31eae30627ef4c7452bd13d67d8bdc86b1c23b&" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();

  setTimeout(function() {
    $('.message.loading').remove();
    $('<div class="message new"><figure class="avatar"><img src="https://cdn.discordapp.com/attachments/875254905554755678/1330781350680199169/20240509_144804_HDR.jpg?ex=678f3a36&is=678de8b6&hm=784754ffda8bb3668a03bd0cff31eae30627ef4c7452bd13d67d8bdc86b1c23b&" /></figure>' + Fake[i] + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
    i++;
  }, 1000 + (Math.random() * 20) * 100);

}
// $(function() {
//   // Sidebar toggle behavior
//   $('#sidebarCollapse').on('click', function() {
//     $('#sidebar, #content').toggleClass('active');
//   });
// });

// Get all elements
var lastId,
    topMenu = $("#sidebar"),
    topMenuHeight = 20,
    menuItems = topMenu.find("a"),
    scrollItems = menuItems.map(function(){
      var item = $($(this).attr("href"));
      if (item.length) { return item; }
    });

// Bind click handler to menu items for fancy scroll animation
menuItems.click(function(e){
  var href = $(this).attr("href"),
      offsetTop = $(href).offset().top-topMenuHeight;
      console.log(offsetTop, topMenuHeight, $(href).offset().top);
  $('html, body').stop().animate({ 
      scrollTop: offsetTop
  }, 300);
  e.preventDefault();
});

function(){
  // Get container scroll position
  var fromTop = $(this).scrollTop()+topMenuHeight;
  
  // Get id of current scroll item
  var cur = scrollItems.map(function(){
    if ($(this).offset().top < fromTop+100)
      return this;
  });
  
  // Get the id of the current element
  cur = cur[cur.length-1];
  var id = cur && cur.length ? cur[0].id : "";
  if (lastId !== id) {
      lastId = id;
      // Set/remove active class
      menuItems
        .removeClass("bg-light")
        .filter("[href='#"+id+"']").addClass("bg-light");
      url = $(location).attr("href");
      url = url.slice(0, url.indexOf('#'))
      // window.location.replace(url+"#"+id);  
      history.pushState("","" ,url+"#"+id);
  }
}

// Bind to scroll
$(window).scroll(function(){
  // Get container scroll position
  var fromTop = $(this).scrollTop()+topMenuHeight;
  
  // Get id of current scroll item
  var cur = scrollItems.map(function(){
    if ($(this).offset().top < fromTop+100)
      return this;
  });
  
  // Get the id of the current element
  cur = cur[cur.length-1];
  var id = cur && cur.length ? cur[0].id : "";
  if (lastId !== id) {
      lastId = id;
      // Set/remove active class
      menuItems
        .removeClass("bg-light")
        .filter("[href='#"+id+"']").addClass("bg-light");
      url = $(location).attr("href");
      url = url.slice(0, url.indexOf('#'))
      // window.location.replace(url+"#"+id);  
      history.pushState("","" ,url+"#"+id);
  }
});

$(document).ready(function(){
  // Get container scroll position
  var fromTop = $(this).scrollTop()+topMenuHeight;
  
  // Get id of current scroll item
  var cur = scrollItems.map(function(){
    if ($(this).offset().top < fromTop+100)
      return this;
  });
  
  // Get the id of the current element
  cur = cur[cur.length-1];
  var id = cur && cur.length ? cur[0].id : "";
  if (lastId !== id) {
      lastId = id;
      // Set/remove active class
      menuItems
        .removeClass("bg-light")
        .filter("[href='#"+id+"']").addClass("bg-light");
      url = $(location).attr("href");
      history.pushState("","" ,url+"#"+id);
  }
});


const hamburger=document.getElementById("mobile_button");let mobileActive=!1;function toggleMobile(){console.log(mobileActive),mobileActive?(mobileActive=!1,hamburger.classList.remove("is-active"),hamburger.setAttribute("aria-expanded","false")):(mobileActive=!0,hamburger.classList.add("is-active"),hamburger.setAttribute("aria-expanded","true"))}hamburger.addEventListener("click",toggleMobile);const observer=lozad();observer.observe(),window.onscroll=function(){checkStick()};const navbar=document.getElementById("navbar"),mobile=document.getElementById("mobile_navbar"),logo=document.getElementById("logo_big"),logo_big=document.getElementById("logo_holder"),logo_icon=document.getElementById("logo_icon"),logo_small=document.getElementById("logo_small"),header=document.getElementById("header"),title=document.getElementById("title"),sticky_title=title.offsetTop,sticky_logo=logo_icon.offsetTop,sticky_icon=logo_big.offsetTop,sticky_nav=navbar.offsetTop-82,sticky_mobile=mobile.offsetTop;function checkStick(){window.pageYOffset>=sticky_title?(title.classList.add("sticky_title"),header.classList.add("sticky_padding"),logo.classList.add("sticky"),logo_icon.classList.add("sticky_fixed"),logo_icon.classList.add("sticky_little"),logo_big.classList.add("asdf"),navbar.classList.add("sticky_nav")):(title.classList.remove("sticky_title"),header.classList.remove("sticky_padding"),logo.classList.remove("sticky"),logo_icon.classList.remove("sticky_fixed"),logo_icon.classList.remove("sticky_little"),navbar.classList.remove("sticky_nav")),sticky_mobile&&(window.pageYOffset>sticky_mobile?mobile.classList.add("sticky_mobile"):mobile.classList.remove("sticky_mobile"))}var act_con="itre",itre=document.getElementById("tab_1"),civil=document.getElementById("tab_2"),former=document.getElementById("tab_3"),itre_staff=document.getElementById("itre_staff"),civil_staff=document.getElementById("civil_staff"),former_staff=document.getElementById("former_staff");function toggleTabContent(e){if(e!==act_con){switch(act_con){case"itre":itre.classList.remove("active_tab"),itre_staff.classList.remove("active_content");break;case"civil":civil.classList.remove("active_tab"),civil_staff.classList.remove("active_content");break;case"former":former.classList.remove("active_tab"),former_staff.classList.remove("active_content")}switch(e){case"itre":itre.classList.add("active_tab"),itre_staff.classList.add("active_content");break;case"civil":civil.classList.add("active_tab"),civil_staff.classList.add("active_content");break;case"former":former.classList.add("active_tab"),former_staff.classList.add("active_content")}act_con=e}}itre&&itre.addEventListener("click",(function(){toggleTabContent("itre")})),civil&&civil.addEventListener("click",(function(){toggleTabContent("civil")})),former&&former.addEventListener("click",(function(){toggleTabContent("former")}));
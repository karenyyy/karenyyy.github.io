(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{24:function(t,e,a){t.exports=a(25)},25:function(t,e,a){"use strict";a.r(e);var n=a(7),r=a(8),i=a(10),c=a(9),o=a(11),s=a(0),l=a.n(s),p=a(18),d=a.n(p),u=a(19),m=a.n(u),h=a(22),f=a(20),b=a(23),g=function(t){function e(){return Object(n.a)(this,e),Object(i.a)(this,Object(c.a)(e).apply(this,arguments))}return Object(o.a)(e,t),Object(r.a)(e,[{key:"render",value:function(){var t="//reddit.com/r/"+this.props.permalink,e="//i.redd.it/"+this.props.url,a="/explore/"+this.props.subreddit;return l.a.createElement(f.a,{style:{padding:"5px"}},l.a.createElement("div",{className:"redcaps-instance card"},l.a.createElement("a",{href:t,target:"_blank"},l.a.createElement("img",{className:"image-div card-img-top img-fluid",src:e,alt:e})),l.a.createElement("div",{className:"caption-div card-body"},l.a.createElement("span",{className:"caption-span card-text"},l.a.createElement("a",{href:a},"r/",this.props.subreddit),": ",this.props.caption))))}}]),e}(s.Component),v=function(t){function e(t){var a;return Object(n.a)(this,e),(a=Object(i.a)(this,Object(c.a)(e).call(this,t))).shuffle=function(t){for(var e=t.length-1;e>0;e--){var a=Math.floor(Math.random()*(e+1)),n=[t[a],t[e]];t[e]=n[0],t[a]=n[1]}return t},a.state={annotations:[]},a}return Object(o.a)(e,t),Object(r.a)(e,[{key:"componentDidMount",value:function(){var t=this;d.a.get("static/homepage_sample.json").then(function(e){e.data=t.shuffle(e.data).slice(0,5),e.data.map(function(e){t.state.annotations.push(l.a.createElement(g,{image_id:e[0],url:e[1],permalink:e[2],caption:e[3],subreddit:e[4]}))}),t.setState({annotations:t.state.annotations})}).catch(function(t){console.log(t)})}},{key:"render",value:function(){return l.a.createElement(h.a,{style:{paddingTop:"5px"}},l.a.createElement(b.a,null,this.state.annotations))}}]),e}(s.Component),E=document.getElementById("root");m.a.render(l.a.createElement(v,null),E)}},[[24,2,1]]]);
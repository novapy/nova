<style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,600);
    body {
        margin:0px;
        font-family: 'Open Sans', 'Tahoma';
        font-size: 14px;
    }

    header ul{
        list-style-type: none;
        padding:0px;
        margin:0px;
    }
    header ul li{
        display: inline-block;
    }
    header ul li a {
        color:#333;
        text-decoration: none;
        display: inline-block;
        padding:15px 10px;
    }
    header ul li a:hover{
        background-color:#F8F8F8;
    }
    
    .bg {
        background: linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%);
        height:350px;
        width:100%;
        box-shadow: 0px 2px 4px #777 inset;
        position:relative;
        overflow:hidden;
    }
    .bg p {
        margin:0px;
        color:#FFF;
        font-size: 30px;
        font-weight: 300;
        text-align: center;
        text-shadow:1px 2px #666;
        width:100%;
    }
    
    #bgCode {
        position:absolute;
        top:350px;
        color:#FFF;
        opacity:0.5;
        font-size:14px;
        animation-name: codeLoop;
        animation-duration: 60s;
        animation-iteration-count: infinite;
        font-family: Consolas;
    }
    @keyframes codeLoop {
        from {top: 350px; opacity:0.5;}
        to {top:-800px; opacity:0.2;}
    }
    
    .grid {
        border-collapse:collapse;
        border:1px solid #EEE;
        width:100%;
    }
    .grid tr td {
        border:1px solid #EEE;
        padding:5px;
        font-size:13px;
        color:#777;
    }
    .grid tr td h3 {
        font-size:14px;
        color:#333;
    }
    .grid tr td h3 label {
        color: #A06001;
    }
    
    .container {max-width:900px;margin:auto;}
    .buttons > span > a { display:inline-block; text-decoration: none; color:#FFF; border:1px solid #FFF; border-radius:3px; padding:8px 12px; font-size:17px;  width:140px; transition: background-color 1s; }
    .buttons > span > a:hover { background-color: rgba(255,255,255,0.5); color: #444; }
    .buttons > span > a:hover ~ div {display:block;}
    .buttons > span > a ~ div{
        height:50px;
        position:absolute;
        overflow:hidden;
        display:none;
        width:335px;
    }
    .buttons > span > a ~ div > div {
        position:absolute;
        top:50px;
        animation-name: hideUp;
        animation-duration: 0.5s;
        animation-fill-mode: forwards;
        color:#444;
        margin:15px 0px;
        text-align:center;
        width:100%;
    }
    @keyframes hideUp {
        from {top: 50px;}
        to {top:0px;}
    }
    
    .center-text { text-align: center }
    .display-block { display:inline-block; }
    
    .max-width-500 { max-width: 500px;}
    .max-width-600 { max-width: 600px;}
    
    .margin-auto {margin:auto !important;}
    .margin-all-20 { margin:20px; }
    
    .padding-all-20 { padding:20px; }
    .padding-all-40 { padding:40px; }
    
</style>

<div class="container">
    <header>
        <ul>
            <li><a href="/">n</a></li>
            <li><a href="/quick-guide">Quick Guide</a></li>
            <li><a href="/library/system">Library</a></li>
        </ul>
    </header>
</div>
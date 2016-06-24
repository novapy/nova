{% include "/app/views/shared/header.tpl" %}

<div class="bg">
    <div id="bgCode">
    </div>
    <div class="container">
        <div class="padding-all-40">
            <p class="max-width-600 margin-auto">novapy is a fast, simple and lightweight CGI micro web-framework for Python.</p>
        </div>

        <div class="center-text">
            <div class="buttons display-block">
                <span>
                    <a href="/download">download</a>
                    <div><div>Download lastest stable release of novapy</div></div>
                </span>
                <span>
                    <a href="https://github.com/novapy/nova">clone on github</a>
                    <div><div>Clone the nightly build of novapy on github</div></div>
                </span>
            </div>
        </div>
    </div>
</div>


<script>
    for(var i=0; i<15; i++){
        rand = Math.random() * (10 -1) + 1;
        console.log(rand)
        div = document.createElement('div');
        div.style.position = 'absolute';
        div.style.width = ((80 * rand) /4) + "px";
        div.style.height = ((80 * rand)/4) + "px";
        div.style.backgroundColor = "#FFF";
        div.style.borderRadius = "1000px"
        var left = 200 * i;
        div.style.left = left + 'px';
        div.style.top = (50*rand) + 'px';
        
        document.getElementById("bgCode").appendChild(div)
    }
</script>
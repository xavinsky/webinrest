function add_onload_js(my_onload_js){
    if(window.attachEvent) {
        window.attachEvent('onload', my_onload_js);
    } else {
        if(window.onload) {
            var prev_onload = window.onload;
            var new_onload = function() {
                prev_onload();
                my_onload_js();
            };
            window.onload = new_onload;
        } else {
            window.onload = my_onload_js;
        }
    }
}

function adapt_internal_links(){
    for (var i = 0; i < document.links.length; i++) {
        el = document.links[i];
        if (el.className=='reference external') {
            if (el.host==location.host) {
                el.className = 'reference internal';
            }
        }
    }
} 

add_onload_js(adapt_internal_links);


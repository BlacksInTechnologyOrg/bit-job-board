from flask_assets import Bundle

common_css = Bundle(
    "css/style.css",
    "css/color.css",
    "components/pg.chocka-blocks/css/cb-general.css",
    "components/pg.chocka-blocks/css/cb-style.css",
    "components/pg.chocka-blocks/css/owl.carousel.css",
    filters="cssmin",
    output="gen/packed.css"
)

common_js = Bundle(
    "js/popper.js",
    "components/pg.chocka-blocks/js/cb-main.js",
    "js/ajaxcalls.js",
    filters="jsmin",
    output="gen/packed.js"
)
$(document).ready(() => {
    scrollClick("mediator", "first");
    scrollClick("protagonist", "second");
    scrollClick("provider", "third");
    scrollClick("virtuoso", "fourth");
    scrollClick("dynamo", "fifth");
});

const scrollClick = (element, target) => {
    $(`#${element}`).click(() => {
        $('html, body').animate({
            scrollTop: $(`#${target}`).offset().top
        }, 800);
    });
}
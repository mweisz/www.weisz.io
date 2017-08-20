function onProjectClick(projectId) {
    
    var project = projectData[projectId];

    // Title
    var title = project['title'];

    // Subtitle
    var subtitle = project['subtitle'];

    // Creators
    var creators = project['creators'];

    // Description
    var description = project['description'];

    // Description Image
    var imgPath = project['imgPath'];

    var projectURL = project['url'];


    var websiteHTML = projectURL ? '<a href="'+projectURL+'">Project Website</a>' : '';
    var html = '<div class="media">' +
                '<h4 class="media-heading">' + title + '</h4>' +
                '<h5 class="media-subheading">By ' + creators + '</h5>' +
              '<div class="media-body">' +
                 '<img class="pull-left description-image" src="' + imgPath +'" alt="...">' +
                description +
              '</div>' +
              '<div class="media-footer">' +
                    '<span class="media-footer-left"></span><span class="media-footer-right">'+ websiteHTML+' </span>' +
              '</div>' +
            '</div>';    

    var dialog = bootbox.dialog({
        message: html,
        onEscape: true,
        backdrop: true,
        size: 'large'
    });
}
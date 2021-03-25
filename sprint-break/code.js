function onOpen() {
    var ui = DocumentApp.getUi();
    ui.createMenu('Find and Replace')
      .addItem('start', 'startFindAndReplace')
      .addToUi();
}


function getFiles() {
    var driveFile = DriveApp.getFileById(DocumentApp.getActiveDocument().getId());
    var parentFoldersIttr = driveFile.getParents();
    var files = [];
    while (parentFoldersIttr.hasNext()) {
        var folder = parentFoldersIttr.next();
        var filesItr = folder.getFiles();
        while (filesItr.hasNext()) {
            var file_item = filesItr.next();
            files.push({ name: file_item.getName(), id: file_item.getId() });
        }
    }
    return files;
}

/*
  Method that replaces search pattern in docs
*/
function replaceText(files, searchPattern, replacement) {
    var errors = [];
    for (var i = 0; i < files.length; i++) {
        try {
          var document = DocumentApp.openById(files[i]);
          var body = document.getBody();
          body.replaceText(searchPattern, replacement);
        }
        catch(e) {
          errors.push({ error: e, file: files[i]});
        }
    }
    if (errors.length > 0) {
        return { error: 'Error', message: 'Some files failed to open.', trace: errors}
    } else {
        return { success: 'Success' }
    }
}

/*
    Starts the image importing process
    @param {string} title side template title
    @return {void}
*/
function startFindAndReplace() {
    var ui = HtmlService.createHtmlOutputFromFile('find_and_replace');
    ui.setTitle('Find and Replace');

    DocumentApp.getUi().showSidebar(ui);
}
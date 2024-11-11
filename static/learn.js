$(document).ready(function() {
    //console.log('lesson_id is: ',lesson_id);
    var currentComponentIndex = 0;
    var components = Object.entries(lesson.components);
    var totalComponents = components.length;
    var lessonImage =$('#component-image')
    var lessonContent =$('#component-content');
    var lesson_id = parseInt(lesson.lesson_id)
    
    function parseComponentText(text) {
        var words = text.split(' ');
        var parsedText = '';

        for (var i = 0; i < words.length; i++) {
            var word = words[i].toLowerCase().replace(/[^\w\s]/gi, ''); // Remove punctuation and make lowercase
            if (vocabulary[word]) {
                parsedText += '<span class="vocab-word" data-toggle="tooltip" data-placement="top" title="' + vocabulary[word] + '">' + words[i] + '</span>';
            } else {
                parsedText += words[i];
            }
            parsedText += ' '; // Add space between words
        }

        return parsedText;
    }

    $('[data-toggle="tooltip"]').tooltip();


    function showComponent(index) {
        var component = components[index][1];
        lessonContent.empty().append('<p><strong>' + component[0] + '</strong> ' + '</p>');
        lessonContent.append('<p>' + parseComponentText(component[1]) + '</p>');
    }
    
    function showImage(index) {
        //Get component of index
        var component = components[index][1];
        //Img name is stored in index 2
        var imgName = component[2];
        //Append imgName to Jinja format
        var imgSrc = "/static/" + imgName;
        //append jinja to html img tag
        var imgSrc='<img src ="'+imgSrc+ '" alt="' + imgName + '">';
        console.log('img path is: ', imgSrc);
        //send imgSrc to learn.html
        lessonImage.empty().append(imgSrc);      
    }

    
    $('#next-btn').click(function() {
        if (currentComponentIndex < totalComponents - 1) {
            currentComponentIndex++;
            showComponent(currentComponentIndex);
            showImage(currentComponentIndex);
            console.log('currentComponentIndex is: ', currentComponentIndex);
        } else {
            console.log('lesson_id is: ', lesson_id)
            var nextLessonId = lesson_id + 1;
            if (nextLessonId) {
                window.location.href = '/learn/' + nextLessonId;
            } else {
                // Handle case where there are no more lessons
                console.log('No more lessons available');
            }
        }
    });

    $('#prev-btn').click(function() {
        
        if (currentComponentIndex > 0) {
            currentComponentIndex--;
            showComponent(currentComponentIndex);
            showImage(currentComponentIndex);
            console.log('currentComponentIndex is: ', currentComponentIndex);
        }
        else {
            if (lesson_id == 1){
                window.location.href = '/';
            }
            else{
                var prevLessonId = lesson_id - 1;
                window.location.href = '/learn/' + prevLessonId;
            }
        }
    });
    showComponent(currentComponentIndex);
    showImage(currentComponentIndex); 
});


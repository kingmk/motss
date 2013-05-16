var threadEditor, replyEditor;
var csrftoken = "";

$(document).ready(function(){
	$('#pub_thread').click(showPubThread);

	$('#th_submit').click(createThread);

	$('#th_cancel').click(hidePubThread);

 	csrftoken = $.cookie('csrftoken');
});

function showPubThread() {
	$('#pub_thread').hide();
	$('#pub_activity').hide();
	$('#thread_form').show();
	threadEditor = new nicEditor({iconsPath : '/static/images/nicEditorIcons.gif', buttonList : ['bold', 'italic', 'strikethrough', 'forecolor', 'left', 'center', 'right', 'link', 'unlink', 'emotion', 'video', 'music'], maxHeight: 215}).panelInstance('th_content');
}

function hidePubThread() {
	if (threadEditor) {
		threadEditor.removeInstance('th_content');
		threadEditor.removePanel('th_content');
		threadEditor = null;
	};
	$('#thread_form').hide();
	$('#pub_thread').show();
	$('#pub_activity').show();
}

function createThread() {
	var title = $('#th_title').val();
	var tags = $('#th_tags').val();
	var content = new nicEditors.findEditor('th_content').getContent();

	$.ajax({
		type : "POST",
		url : "/post/createthread/",
		data : {
			'title' : title,
			'tags' : tags,
			'content' : content,
			'csrfmiddlewaretoken' : csrftoken
		},
		dataType : 'json',
		success : function(data) {
			hidePubThread();
		},
		error : function(xhr) {

		}
	});
}
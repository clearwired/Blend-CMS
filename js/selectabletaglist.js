Array.prototype.isEmpty = function(){
	if( this.length == 0) return true;
	return false;
}


var SelectableTagList = Class.create({
	initialize: function( options ) {
		this.list = $( options.selectable_tag_list );
		this.links = this.list.select('a');
		this.appendee = $( options.field );
		this.appendee_type = this.getAppendeeType( this.appendee );
		this.selected_tags = [];
		this.selected_tags_container = $( options.selected_tags_container );
		this.selected_tags_list = new Element('ul');
		this.remove_text = options.remove_text;
		this.setupBehaviour();
		this.initial_tags = $A(options.initial_tags) || [];
		if(!this.initial_tags.isEmpty()) { this.populateInitialTags();}
	},

	setupBehaviour: function() {
		var oThis = this;
		// Add click events to the tag links
		this.links.each( function( link ) {
			link.observe('click', oThis.tagClick.bindAsEventListener( oThis ));
		});
	},
	
	populateInitialTags: function(){
		// Create our ul tag for our generated list if it hasnt been created yet
		if( this.selected_tags_container.childElements().isEmpty()) this.createSelectedTagsList();
		this.selected_tags = this.selected_tags.concat( this.initial_tags )
		this.writeTagsToField( this.selected_tags );
		
		// Generate our list items for pre-populated tags
		var oThis = this;
		this.selected_tags.each( function( tagname ){
			var remove_link = new Element('a',{href:"#", tag: tagname}).update( oThis.remove_text );
				remove_link.observe('click', oThis.removeClick.bindAsEventListener( oThis ));
			oThis.selected_tags_list.insert( new Element('li').update( tagname ).insert( remove_link ));
		});
	},
	
	tagClick: function( event ){
		this.addTag( Event.element(event).firstChild.nodeValue )
		event.stop();
	},			
	
	getAppendeeType: function( appendee ){
		if( appendee.nodeType == 1 && appendee.nodeName.toLowerCase() == "input" && appendee.readAttribute('type').toLowerCase() == "hidden" ) {
			 return "hidden";
		}
	},
	
	addTag: function( tagname ){
		this.selected_tags.push( tagname );
		this.writeTagsToField( this.selected_tags );
		
		// Create our ul tag for our generated list if it hasnt been created yet
		if( this.selected_tags_container.childElements().isEmpty()) this.createSelectedTagsList();
		
		// Add remove capabilities to our generated list
		// custom attribute of :tag - allows us to retrieve the tag value
		// to be removed from the generated selected tags array.
		
		var remove_link = new Element('a',{href:"#", tag: tagname}).update( this.remove_text );
				remove_link.observe('click', this.removeClick.bindAsEventListener( this ));
		this.selected_tags_list.insert( new Element('li').update( tagname ).insert( remove_link ));
	},
	
	removeTag: function( tagname ){
		this.selected_tags = this.selected_tags.without( tagname );
		if( this.selected_tags.isEmpty()) this.selected_tags_list.remove();
		this.writeTagsToField( this.selected_tags );
	},
	
	writeTagsToField: function( tags ){
		switch( this.appendee_type ){
			case "hidden":
				this.appendee.writeAttribute( 'value' , tags.join('\n') );
				break;
		}
	},
	
	removeClick: function( event ) {
		var link = Event.element(event);
		this.removeTag( link.getAttribute('tag'));
		var parent_li = link.up().remove();
		event.stop();
	},
	
	createSelectedTagsList: function(){
		this.selected_tags_container.insert( this.selected_tags_list);
	}
})
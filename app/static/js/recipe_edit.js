/*
* @Author: Stefan Lehmann
* @Date:   2016
* @Last Modified by:   Stefan Lehmann
* @Last Modified time: 2016
*/

$(document).ready(function() {
  // add malt
  $('a.add-malt').click(function(event) {
    var last_div = ($('.malt-div')).last()
    new_div = last_div.clone(true, true).appendTo('.malt-body')
    new_num = parseInt(new_div.attr('id').match(/\d+/)) + 1

    new_div.attr('id', "malt-" + new_num);
    new_div.find("input[id*='name_']").attr('id', 'malts-' + new_num + '-name_')
    new_div.find("input[id*='name_']").attr('name', 'malts-' + new_num + '-name_')
    new_div.find("input[id*='qty']").attr('id', 'malts-' + new_num + '-qty')
    new_div.find("input[id*='qty']").attr('name', 'malts-' + new_num + '-qty')

    event.stopPropagation();
  });

  // remove malt
  $('.del-malt').click(function() {
      if ($('.malt-div').length > 1) {
          var thisRow = $(this).closest(".malt-div");
          thisRow.remove();
      }
  }); //End remove row


  // add hop
  $('a.add-hop').click(function(event) {
    var last_div = ($('.hop-div')).last()
    new_div = last_div.clone(true, true).appendTo('.hop-body')
    new_num = parseInt(new_div.attr('id').match(/\d+/)) + 1

    new_div.attr('id', "hop-" + new_num);
    new_div.find("input[id*='name_']").attr('id', 'hops-' + new_num + '-name_')
    new_div.find("input[id*='name_']").attr('name', 'hops-' + new_num + '-name_')
    new_div.find("input[id*='qty']").attr('id', 'hops-' + new_num + '-qty')
    new_div.find("input[id*='qty']").attr('name', 'hops-' + new_num + '-qty')

    event.stopPropagation();
  });

  // remove malt
  $('.del-hop').click(function() {
      if ($('.hop-div').length > 1) {
          var thisRow = $(this).closest(".hop-div");
          thisRow.remove();
      }
  }); //End remove row

    // add misc ingredient
  $('a.add-misc').click(function(event) {
    console.log('click');
    var last_div = $('.misc-div').last();
    new_div = last_div.clone(true, true).appendTo('.misc-body');
    new_num = parseInt(new_div.attr('id').match(/\d+/)) + 1;

    new_div.attr('id', 'misc-' + new_num);
    new_div.find("input[id*='name_']").attr('id', 'misc-' + new_num + '-name_')
    new_div.find("input[id*='name_']").attr('name', 'misc-' + new_num + '-name_')
    new_div.find("input[id*='qty']").attr('id', 'misc-' + new_num + '-qty')
    new_div.find("input[id*='qty']").attr('name', 'misc-' + new_num + '-qty')
    event.stopPropagation();
  })

  // remove misc ingredient
  $('.del-misc').click(function() {
    if ($('.misc-div').length > 0) {
      var row = $(this).closest('.misc-div');
      row.remove();
    }
  });
});
/*
* @Author: Stefan Lehmann
* @Date:   2016
* @Last Modified by:   lehmann
* @Last Modified time: 2016
*/

$(document).ready(function() {

  var div_template =
    '<div class="entry-div col-sm-12">' +
      '<div class="form-horizontal">' +
          '<div class="form-group">' +
            '<div class="col-sm-6">' +
              '<input class="form-control">' +
            '</div>' +
            '<div class="col-sm-2">' +
              '<div class="input-group">' +
                '<input class="form-control">' +
                '<div class="input-group-addon" style="width:30px"></div>' +
              '</div>' +
            '</div>' +
            '<a class="btn btn-link"><span class="glyphicon glyphicon-trash"></span></a>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</div>'


  function add_entry(type, nr) {
    html = $.parseHTML(div_template);
    $('.' + type + '-body').append(html);
    $div = $('.' + type + '-body .entry-div').last();

    $div.attr('id', type + '-' + nr);

    // name input
    $name_input = $div.find('input').eq(0);
    $name_input.attr('id', type + '-' + nr + '-name_');
    $name_input.attr('name', type + '-' + nr + '-name_');

    // quantity input
    $qty_input = $div.find('input').eq(1);
    $qty_input.attr('id', type + '-' + nr + '-qty');
    $qty_input.attr('name', type + '-' + nr + '-qty');
  }


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
  // $('a.add-misc').click(function(event) {
  //   var last_div = $('.misc-div').last();
  //   new_div = last_div.clone(true, true).appendTo('.misc-body');
  //   new_num = parseInt(new_div.attr('id').match(/\d+/)) + 1;

  //   new_div.attr('id', 'misc-' + new_num);
  //   new_div.find("input[id*='name_']").attr('id', 'misc-' + new_num + '-name_')
  //   new_div.find("input[id*='name_']").attr('name', 'misc-' + new_num + '-name_')
  //   new_div.find("input[id*='qty']").attr('id', 'misc-' + new_num + '-qty')
  //   new_div.find("input[id*='qty']").attr('name', 'misc-' + new_num + '-qty')
  //   event.stopPropagation();
  // })

  $('a.add-misc').click(function(event) {
    var $entries = $('.misc-body .entry-div');
    var nr = 0
    if ($entries.length > 0) {
      nr = parseInt($entries.last().attr('id').match(/\d+/)) + 1;
    }
    add_entry('misc', nr);
    // new_div.attr('id', "malt-" + new_num);
    // new_div.find("input[id*='name_']").attr('id', 'malts-' + new_num + '-name_')
    // new_div.find("input[id*='name_']").attr('name', 'malts-' + new_num + '-name_')
    // new_div.find("input[id*='qty']").attr('id', 'malts-' + new_num + '-qty')
    // new_div.find("input[id*='qty']").attr('name', 'malts-' + new_num + '-qty')
    event.stopPropagation();
  });

  // remove misc ingredient
  $('.del-misc').click(function() {
    if ($('.misc-div').length > 0) {
      var row = $(this).closest('.misc-div');
      row.remove();
    }
  });
});
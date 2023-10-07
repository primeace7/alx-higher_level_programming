// adds, removes and clears LI elements from a list when the user clicks
$(document).ready(() => {
  $('div#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').on('click', () => {
    const collection = $('ul.my_list li');
    const lastItem = collection.last();
    lastItem.remove();
  });

  $('div#clear_list').on('click', () => {
    const collection = $('ul.my_list li');
    collection.remove();
  });
});

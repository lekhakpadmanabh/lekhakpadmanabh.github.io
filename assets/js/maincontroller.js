app.controller("MainController", function($scope){
  $scope.selectedNoteId = 0;
  $scope.setActive = function(id) {
    $scope.selectedNoteId = id;
  };
  $scope.data = {
    "count": 2,
    "title": "My Blog",
    "author": "Padmanabh",
    "notes": [
        {
        "id": 0,
        "date": "1234",
        "title": "Post no 1",
        "tags": ["test","padmanabh","javascript"],
        "content": "<p>this is the actual post</p>",
        },
        {
        "id":1,
        "date": "1235",
        "title": "Post no 2",
        "tags": ["test","jdfop","javascript"],
        "content": "<p>this is the actual post no2</p>",
        },
    ]
    };


});

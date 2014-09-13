app.controller("MainController", function($scope, $http){
  $scope.selectedNoteId = 0;
  $scope.setActive = function(id) {
    $scope.selectedNoteId = id;
  };
  $http.get('data.json').then(function(rest){
    $scope.data = res.data
  });
  

});

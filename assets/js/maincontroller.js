app.controller("MainController", function($scope, $http, $sce){
  $scope.selectedNoteId = 0;
  $scope.setActive = function(id) {
    $scope.selectedNoteId = id;
  };
  $http.get('data.json').then(function(res){
    $scope.data = res.data
  });
  $scope.trustDodgyHTML = function(html) {
      return $sce.trustAsHtml(html);
    };

});

{
  formatter: function () {
      // The first returned item is the header, subsequent items are the
      // points
      return ['<b>' + this.x + '</b>'].concat(
          this.points ?
              this.points.map(function (point) {
                  return point.series.name + ': ' + point.y + 'm';
              }) : []
      );
  },
  split: true
}

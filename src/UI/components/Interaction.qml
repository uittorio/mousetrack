import QtQuick

Rectangle {
    id: container
    property alias text: label.text
    property string image: ""
    property string countText: ""
    height: 50
    width: 200

    Row {
        Image {
            id: image
            source: container.image;
            fillMode: Image.PreserveAspectFit
            height: container.height
        }

        Text {
            id: label
            anchors.left: image.right
            anchors.verticalCenter: image.verticalCenter;
            text: text
            font.family: "Nunito"
            font.weight: 200
            font.pointSize: 12
            color: "#1D1D1D"
        }

        Text {
            id: count
            text: countText
            anchors.left: label.right
            anchors.leftMargin: 20
            anchors.verticalCenter: image.verticalCenter;
            anchors.horizontalCenter: image.horizontalCenter;
            font.family: "Nunito"
            font.weight: 300
            font.pointSize: 16
            color: "#1D1D1D"
        }
    }
}
import React from 'react';
import { shallow } from 'enzyme';
import ExampleWork, { ExampleWorkBubble } from '../js/example-work'

const myWork = [
    {
        'title': "Work Example",
        "image": {
            "desc": "example screenshot of a project involving code",
            "src": "images/example1.png",
            "comment": ""
        }
    },
    {
        'title': "Portfolio Web",
        "image": {
            "desc": "A Serverless Portfolio",
            "src": "images/portfolio.png",
            "comment": ""
        }
    }
];

describe("Examplework component", () => {
    let component = shallow(<ExampleWork work={myWork}/>);

    it("Should be a 'section' element", () => {
        expect(component.type()).toEqual('section');
    });

    it("Should contain as many children as work examples", () => {
        expect(component.find("ExampleWorkBubble").length).toEqual(myWork.length);
    });
});

describe("ExampleWorkBubble component", () => {
    let component = shallow(<ExampleWorkBubble example={myWork[1]}/>);

    let images = component.find("img");
    it("Should contain a single image element", () => {
        expect(images.length).toEqual(1);
    });

    it("Should have the image src set correctly", () => {
        expect(images.node.props.src).toEqual(myWork[1].image.src);
    });
});

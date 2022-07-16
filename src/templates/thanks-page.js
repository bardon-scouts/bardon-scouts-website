import React from "react";
import PropTypes from "prop-types";
import { graphql } from "gatsby";
import Layout from "../components/Layout";
import Content, { HTMLContent } from "../components/Content";
import FullWidthImage from "../components/FullWidthImage";
import { getImage } from "gatsby-plugin-image";
import logo from "../img/scouts_logo.jpg";

// eslint-disable-next-line
export const ThanksTemplate = ({ title, image,subheading, content, contentComponent }) => {
  const PageContent = contentComponent || Content;
  const heroImage = getImage(image) || image;
  //const title = post.frontmatter.title;
  return (

    <section className="section">
      <div className="scouts-logo"><img src={logo} alt="Scouts Australia" /></div>
      <FullWidthImage img={heroImage} title={title} subheading={subheading} />
      <div className="container">
        <div className="content">
          <h1>{title}</h1>
          <PageContent className="content" content={content} />
        </div>
        <p><a href="/">&lt; Back</a></p>
      </div>
    </section>


  );
};

ThanksTemplate.propTypes = {
  title: PropTypes.string.isRequired,
  subheading: PropTypes.string,
  image: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
  content: PropTypes.string,
  contentComponent: PropTypes.func,
};

const Thanks = ({ image,data }) => {
  const { markdownRemark: post } = data;
  return (
    <Layout>

      <ThanksTemplate
        contentComponent={HTMLContent}
        title={post.frontmatter.title}
        content={post.html}
        image={post.frontmatter.image}
        subheading={post.frontmatter.subheading}
      />
    </Layout>
  );
};

Thanks.propTypes = {
  data: PropTypes.object.isRequired
};

export default Thanks;

export const thanksQuery = graphql`
  query Thanks($id: String!) {
    markdownRemark(id: { eq: $id }) {
      html
      frontmatter {
        title
        subheading
        image {
          childImageSharp {
            gatsbyImageData(quality: 100, layout: FULL_WIDTH)
          }
        }
      }
    }
  }
`;

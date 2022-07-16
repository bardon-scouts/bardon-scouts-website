import React from "react";
import PropTypes from "prop-types";
import { graphql } from "gatsby";
import Layout from "../components/Layout";
import Content, { HTMLContent } from "../components/Content";

// eslint-disable-next-line
export const ContactUsTemplate = ({ title, content, contentComponent }) => {
  const PageContent = contentComponent || Content;

  return (

    <section className="section">
      <div className="container">
        <div className="content">
          <h1>{title}</h1>
          <PageContent className="content" content={content} />
          <form
              name="contact"
              method="post"
              action="/contact/thanks/"
              data-netlify="true"
              data-netlify-honeypot="bot-field"
          >
            {/* The `form-name` hidden field is required to support form submissions without JavaScript */}
            <input type="hidden" name="form-name" value="contact" />
            <div hidden>
              <label>
                Don’t fill this out:{" "}
                <input name="bot-field" />
              </label>
            </div>
            <div className="field">
              <label className="label" htmlFor={"name"}>
                Your name
              </label>
              <div className="control">
                <input
                    className="input"
                    type={"text"}
                    name={"name"}
                    id={"name"}
                    required={true}
                />
              </div>
            </div>
            <div className="field">
              <label className="label" htmlFor={"email"}>
                Email
              </label>
              <div className="control">
                <input
                    className="input"
                    type={"email"}
                    name={"email"}
                    id={"email"}
                    required={true}
                />
              </div>
            </div>

            <div className="field">
              <label className="label" htmlFor={"message"}>
                Message
              </label>
              <div className="control">
                    <textarea
                        className="textarea"
                        name={"message"}
                        id={"message"}
                        required={true}
                    />
              </div>
            </div>
            <div className="field">
              <button type="submit">Send</button>
            </div>
            <p><a href="/">&lt; Back</a></p>

          </form>
        </div>
      </div>
    </section>


  );
};

ContactUsTemplate.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string,
  contentComponent: PropTypes.func,
};

const ContactUs = ({ data }) => {
  const { markdownRemark: post } = data;

  return (
    <Layout>
      <ContactUsTemplate
        contentComponent={HTMLContent}
        title={post.frontmatter.title}
        content={post.html}
      />
    </Layout>
  );
};

ContactUs.propTypes = {
  data: PropTypes.object.isRequired,
};

export default ContactUs;

export const contactUsQuery = graphql`
  query ContactUs($id: String!) {
    markdownRemark(id: { eq: $id }) {
      html
      frontmatter {
        title
      }
    }
  }
`;
